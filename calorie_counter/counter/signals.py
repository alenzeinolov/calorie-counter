from django.db import models
from django.db.models import Sum
from django.dispatch import receiver

from .models import CalorieRecord


@receiver(models.signals.pre_save, sender=CalorieRecord)
def calculate_on_goal(sender, instance, *args, **kwargs):
    daily_goal = instance.user.daily_calorie_goal
    records = CalorieRecord.objects.filter(user=instance.user, date__date=instance.date.date())

    total = records.aggregate(total=Sum('calories'))['total']
    if total is None:
        total = 0

    try:
        check_record = CalorieRecord.objects.get(pk=instance.pk)
        total = total - check_record.calories
    except CalorieRecord.DoesNotExist:
        pass
    total += instance.calories

    on_goal = total <= daily_goal
    records.update(on_goal=on_goal)
    instance.on_goal = on_goal


# TODO: Signal to update on_goal on calorie record deletion
