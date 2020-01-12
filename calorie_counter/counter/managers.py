from django.db import models
from django.db.models import Sum


class CalorieRecordManager(models.Manager):

    def recalculate_on_target(self, user):
        daily_goal = user.daily_calorie_goal
        records = self.filter(user=user)
        dates_with_records = records.dates('date', kind='day')
        for date in dates_with_records:
            current_records = records.filter(date__date=date)
            total = current_records.aggregate(total=Sum('calories'))['total']
            on_target = total <= daily_goal
            self.apply_on_target(current_records, on_target)

    def apply_on_target(self, records, on_target):
        records.exclude(on_target=on_target).update(on_target=on_target)
