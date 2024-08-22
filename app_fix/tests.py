# app_fix/tests/test_models.py

from django.test import TestCase
from django.utils import timezone

from .models import Logs


class LogsModelTest(TestCase):

    def setUp(self):
        self.log = Logs.objects.create(
            ip_address="192.168.1.1",
            date=timezone.now(),
            method="GET",
            uri="/path/path",
            resp_code=200,
            resp_bytes=6,
        )

    def test_logs_str(self):
        self.assertEqual(
            str(self.log),
            f"{self.log.ip_address} - {self.log.date} - {self.log.resp_code}",
        )

    def test_ip_address(self):
        self.assertEqual(self.log.ip_address, "192.168.1.1")

    def test_date(self):
        self.assertIsNotNone(self.log.date)

    def test_method(self):
        self.assertEqual(self.log.method, "GET")

    def test_uri(self):
        self.assertEqual(self.log.uri, "/path/path")

    def test_resp_code(self):
        self.assertEqual(self.log.resp_code, 200)

    def test_resp_bytes(self):
        self.assertEqual(self.log.resp_bytes, 6)
