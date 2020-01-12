from django.urls import path

from .api.views import CalorieRecordReportView, UserReportView

app_name = 'reports'
urlpatterns = [
    path('records/', CalorieRecordReportView.as_view(), name='records'),
    path('users/', UserReportView.as_view(), name='users'),
]