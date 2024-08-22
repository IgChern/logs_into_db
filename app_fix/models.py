from django.db import models


class Logs(models.Model):
    ip_address = models.GenericIPAddressField()
    date = models.DateTimeField()
    method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    resp_code = models.PositiveIntegerField()
    resp_bytes = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.ip_address} - {self.date} - {self.resp_code}"
