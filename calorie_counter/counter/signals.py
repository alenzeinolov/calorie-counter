from django.db import models
from django.db.models import Sum
from django.dispatch import receiver

from .models import CalorieRecord


@receiver(models.signals.pre_save, sender=CalorieRecord)
def calculate_on_target(sender, instance, *args, **kwargs):
    daily_goal = instance.user.daily_calorie_goal
    records = CalorieRecord.objects.filter(user=instance.user, date__date=instance.date.date())
    total = records.aggregate(total=Sum('calories'))['total']
    check_record = CalorieRecord.objects.filter(pk=instance.pk)
    if not check_record.exists():
        total += instance.calories
        print('it does not exist')
    print(total)
    print(daily_goal)
    if total <= daily_goal:
        records.update(on_target=True)
        instance.on_target = True
    records.update(on_target=False)
    instance.on_target = False
    print('I AM EXECUTING')
