from django.contrib import admin

from .models import Logs


# Register your models here.
@admin.register(Logs)
class LogsAdm(admin.ModelAdmin):
    list_display = (
        "ip_address",
        "date",
        "method",
    )
    list_filter = (
        "ip_address",
        "resp_code",
    )
    search_fields = (
        "resp_code",
        "method",
        "resp_bytes",
    )
