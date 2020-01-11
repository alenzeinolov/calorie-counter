from django.urls import path

from calorie_counter.accounts.api.views import UserCreateView, UserUpdateView

app_name = 'accounts'
urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('set_goal/', UserUpdateView.as_view(), name='set_goal'),
]