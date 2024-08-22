from rest_framework import filters, viewsets

from .models import Logs
from .serializers import LogsSerializer


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["method", "uri"]
    ordering_fields = ["date", "method", "uri", "resp_code", "resp_bytes"]
    ordering = ["date"]
