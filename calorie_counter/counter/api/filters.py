import django_filters

from ..models import CalorieRecord


class CalorieRecordFilterSet(django_filters.FilterSet):
    calories = django_filters.RangeFilter()
    date = django_filters.DateFromToRangeFilter(lookup_expr='date')

    class Meta:
        model = CalorieRecord
        fields = ('user', 'calories')
