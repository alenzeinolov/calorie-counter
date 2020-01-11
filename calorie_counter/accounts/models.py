import uuid

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    daily_calorie_goal = models.PositiveIntegerField(
        _('daily calorie goal'),
        default=2000,
        validators=[
            validators.MinValueValidator(500),
        ]
    )
