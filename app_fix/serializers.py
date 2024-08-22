from rest_framework import serializers

from .models import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ["ip_address", "date", "method", "uri", "resp_code", "resp_bytes"]
