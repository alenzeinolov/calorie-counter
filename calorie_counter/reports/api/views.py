from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from calorie_counter.counter.models import CalorieRecord
from calorie_counter.counter.api.filters import CalorieRecordFilterSet


class CalorieRecordReportView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        records = CalorieRecord.objects.all()
        calorie_record_filter = CalorieRecordFilterSet(request.query_params, queryset=records)
        filtered_records = calorie_record_filter.qs

        response = CalorieRecord.objects.get_combined_aggregations(filtered_records)

        return Response(response)


class UserReportView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        date_str = request.query_params.get('date', None)
        if date_str is not None:
            date = timezone.datetime.strptime(date_str, '%Y-%m-%d')
        else:
            date = timezone.datetime.today()

        response = dict()
        response['num_users_exceeded_goal'] = CalorieRecord.objects.get_num_users_exceeded_goal(date)

        return Response(response)
