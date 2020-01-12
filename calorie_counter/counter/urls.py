from rest_framework.routers import DefaultRouter

from calorie_counter.counter.api.viewsets import CalorieRecordViewSet

router = DefaultRouter()
router.register('records', CalorieRecordViewSet, basename='calorie_record')

app_name = 'counter'
urlpatterns = [

] + router.urls
