from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from calorie_counter.counter.api.viewsets import CalorieRecordViewSet

User = get_user_model()


class CalorieRecordTestCase(APITestCase):

    def setUp(self):

        self.data_1 = {
            'calories': 500,
            'comment': 'Завтрак',
            'date': '2020-01-01T09:00',
        }

        self.data_2 = {
            'calories': 1000,
            'comment': 'Обед',
            'date': '2020-01-01T13:00',
        }

        self.data_3 = {
            'calories': 600,
            'comment': 'Ужин',
            'date': '2020-01-01T19:00',
        }

        self.factory = APIRequestFactory()

        self.test_user_1 = User.objects.create_user('user1', 'user1@example.com', 'user1pwd')
        self.test_user_2 = User.objects.create_user('user2', 'user2@example.com', 'user2pwd')

        self.test_user_1.daily_calorie_goal = 2000
        self.test_user_2.daily_calorie_goal = 3000

        self.test_user_1.save()
        self.test_user_2.save()

        self.calorie_record_url = reverse('counter:calorie_record-list')

    def test_create_records(self):
        view = CalorieRecordViewSet.as_view({'post': 'create'})

        # Create for user 1
        request = self.factory.post(self.calorie_record_url, data=self.data_1, format='json')
        force_authenticate(request, user=self.test_user_1)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_1['calories'])
        self.assertEqual(response.data['comment'], self.data_1['comment'])

        request = self.factory.post(self.calorie_record_url, data=self.data_2, format='json')
        force_authenticate(request, user=self.test_user_1)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_2['calories'])
        self.assertEqual(response.data['comment'], self.data_2['comment'])

        request = self.factory.post(self.calorie_record_url, data=self.data_3, format='json')
        force_authenticate(request, user=self.test_user_1)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_3['calories'])
        self.assertEqual(response.data['comment'], self.data_3['comment'])

        # Create for user 2
        request = self.factory.post(self.calorie_record_url, data=self.data_1, format='json')
        force_authenticate(request, user=self.test_user_2)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_1['calories'])
        self.assertEqual(response.data['comment'], self.data_1['comment'])

        request = self.factory.post(self.calorie_record_url, data=self.data_2, format='json')
        force_authenticate(request, user=self.test_user_2)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_2['calories'])
        self.assertEqual(response.data['comment'], self.data_2['comment'])

        request = self.factory.post(self.calorie_record_url, data=self.data_3, format='json')
        force_authenticate(request, user=self.test_user_2)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['calories'], self.data_3['calories'])
        self.assertEqual(response.data['comment'], self.data_3['comment'])

    def test_count_and_on_goal(self):
        view = CalorieRecordViewSet.as_view({'get': 'list'})

        self.test_create_records()

        filter_str = '?user={0}'.format(self.test_user_1.id)
        request = self.factory.get(self.calorie_record_url + filter_str)
        force_authenticate(request, user=self.test_user_1)
        response = view(request)

        # 3 elements created for test user 1
        self.assertEqual(len(response.data['results']), 3)
        # User 1 has goal of 2000 calories, but entries exceed the value
        self.assertFalse(response.data['results'][0]['on_goal'])

        filter_str = '?user={0}'.format(self.test_user_2.id)
        request = self.factory.get(self.calorie_record_url + filter_str)
        force_authenticate(request, user=self.test_user_2)
        response = view(request)

        # 3 elements created for test user 2
        self.assertEqual(len(response.data['results']), 3)
        # User 2 has goal of 3000 calories, and entries should not exceed value
        self.assertTrue(response.data['results'][0]['on_goal'])

