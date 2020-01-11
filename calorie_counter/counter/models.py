import uuid

from django.conf import settings
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class CalorieRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='records',
        related_query_name='record',
    )
    calories = models.PositiveIntegerField(
        _('calories'),
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    comment = models.TextField(
        _('comment'),
        default='',
        blank=True,
    )
    date = models.DateTimeField(_('date'))

    class Meta:
        verbose_name = _('calorie record')
        verbose_name_plural = _('calorie records')
