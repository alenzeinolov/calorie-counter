from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import CalorieRecord

User = get_user_model()


class CalorieRecordSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = CalorieRecord
        fields = ('id', 'user', 'calories', 'comment', 'on_goal', 'date')
        read_only_fields = ('on_goal', )
