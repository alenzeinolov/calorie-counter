from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import User
from ...counter.models import CalorieRecord


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'daily_calorie_goal', 'password')

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            daily_calorie_goal=validated_data['daily_calorie_goal'],
            password=validated_data['password'],
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    daily_calorie_goal = serializers.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'daily_calorie_goal')
        read_only_fields = ('username', 'email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        instance = super(UserUpdateSerializer, self).update(instance, validated_data)
        CalorieRecord.objects.recalculate_on_goal(instance)
        return instance
