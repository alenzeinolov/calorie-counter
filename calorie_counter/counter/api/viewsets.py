from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import CalorieRecordFilterSet
from .serializers import CalorieRecordSerializer
from ..models import CalorieRecord


class CalorieRecordViewSet(ModelViewSet):
    queryset = CalorieRecord.objects.all()
    serializer_class = CalorieRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CalorieRecordFilterSet
    pagination_class = PageNumberPagination
