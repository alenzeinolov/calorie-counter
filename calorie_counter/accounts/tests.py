from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory

from .api.views import UserUpdateView

User = get_user_model()


class UserTestCase(APITestCase):

    def setUp(self):
        self.test_user = User.objects.create_user('TestUser', 'test@user@.com', 'testpassword')

        self.register_url = reverse('accounts:register')
        self.set_goal_url = reverse('accounts:set_goal')

    def test_register_user(self):

        data = {
            'username': 'user1',
            'first_name': 'user',
            'last_name': '1',
            'email': 'user1@example.com',
            'password': 'user1password',
            'daily_calorie_goal': 2500,
        }

        response = self.client.post(self.register_url, data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['daily_calorie_goal'], data['daily_calorie_goal'])
        self.assertFalse('password' in response.data)

    def test_set_goal(self):
        factory = APIRequestFactory()
        view = UserUpdateView.as_view()

        data = {
            'daily_calorie_goal': 3000,
        }
        request = factory.put(self.set_goal_url, data, format='json')
        force_authenticate(request, user=self.test_user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['daily_calorie_goal'], data['daily_calorie_goal'])
