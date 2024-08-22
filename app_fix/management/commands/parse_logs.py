import json
import logging
from datetime import datetime
from io import StringIO

import requests
from django.core.management.base import BaseCommand

from app_fix.models import Logs

logger = logging.getLogger("django")


class Command(BaseCommand):
    help = "Add your logs"

    @staticmethod
    def parse_time(time_str):
        try:
            # Преобразование строки времени в объект datetime
            return datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z")
        except ValueError as e:
            logger.error(f"Error parsing time '{time_str}': {e}")
            return None

    def add_arguments(self, parser):
        parser.add_argument("file_url", type=str)

    def handle(self, *args, **options):
        data = options["file_url"]
        # Запрос данных из url
        response = requests.get(data)
        response.raise_for_status()
        text_io = StringIO(response.text)

        # Обработка каждой строки из ответа
        for line in text_io:
            line = line.strip()
            if not line:
                continue
            try:
                log_data = json.loads(line)
                time = self.parse_time(log_data.get("time"))
                Logs.objects.create(
                    ip_address=log_data.get("remote_ip"),
                    date=time,
                    method=log_data.get("request").split(" ")[0],
                    uri=log_data.get("request").split(" ")[1],
                    resp_code=log_data.get("response"),
                    resp_bytes=log_data.get("bytes"),
                )
            except json.JSONDecodeError as e:
                logger.error(f"Error process json.loads: {e}")
            except Exception as e:
                logger.error(f"Error process line: {e}")

        self.stdout.write(self.style.SUCCESS("Successfully imported log data"))
