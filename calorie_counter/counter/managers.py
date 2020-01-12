from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.db.models import Sum, Avg, Max

User = get_user_model()


class CalorieRecordManager(models.Manager):

    def recalculate_on_goal(self, user):
        daily_goal = user.daily_calorie_goal
        records = self.filter(user=user)
        dates_with_records = records.dates('date', kind='day')
        for date in dates_with_records:
            current_records = records.filter(date__date=date)
            total = current_records.aggregate(total=Sum('calories'))['total']
            on_goal = total <= daily_goal
            self.apply_on_goal(current_records, on_goal)

    def apply_on_goal(self, records, on_goal):
        records = records.select_for_update().exclude(on_goal=on_goal)
        with transaction.atomic():
            records.update(on_goal=on_goal)

    def get_num_users_exceeded_goal(self, date):
        records = self.filter(date__date=date, on_goal=False)
        users = User.objects.filter(record__in=records)
        return users.distinct().count()

    def get_max_calories_date(self, records):
        return records.aggregate(max=Max('calories'))['max']

    def get_avg_calories(self, records):
        return records.aggregate(average=Avg('calories'))['average']

    def get_total_calories(self, records):
        return records.aggregate(total=Sum('calories'))['total']

    def get_combined_aggregations(self, records):
        return records.aggregate(
            total_calories=Sum('calories'),
            avg_calories=Avg('calories'),
            max_calories=Max('calories'),
        )
