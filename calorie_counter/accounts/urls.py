from django.urls import path

from calorie_counter.accounts.api.views import UserCreateView, UserUpdateView, UserRetrieveView

app_name = 'accounts'
urlpatterns = [
    path('info/', UserRetrieveView.as_view(), name='info'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('set_goal/', UserUpdateView.as_view(), name='set_goal'),
]