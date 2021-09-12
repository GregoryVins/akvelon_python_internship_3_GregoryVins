from django.test import TestCase
from rest_framework import status

from custom_user.models import CustomUser
from custom_user.serializers import CustomUserSerializer


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.url = '/api/users/'
        self.user = CustomUser.objects.create(first_name='Test', last_name='Testov', email="test@example.local")

    def test_get_user_list(self):
        """
        Request users list.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        """
        Request user detail information.
        """
        response = self.client.get(f'{self.url}{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CustomUserSerializer(self.user).data)

    def test_create_user_success(self):
        """
        Creating of new user completed successfully.
        """
        data = {
            'first_name': 'User',
            'last_name': 'Userov',
            'email': 'Userovich@example.local',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_fail(self):
        """
        Creating of new user completed failed.
        """
        data = {
            'first_name': 'User',
            'email': 'Userovich',
        }
        response = self.client.post(self.url, data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_user_success(self):
        """
        Successful edit user data.
        """
        data = {
            'first_name': 'CustomUser',
            'last_name': 'CustomUserob',
            'email': 'CustomUser@example.local',
        }
        response = self.client.put(f'{self.url}{self.user.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_user_fail(self):
        """
        Failed edit user data.
        """
        data = {
            'first_name': 'CustomUser~',
            'last_name': 'CustomUserob¨¼Â',
            'email': 'CustomUser11111',
        }
        response = self.client.put(f'{self.url}{self.user.id}/', data, content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user_success(self):
        """
        Success user deleting.
        """
        response = self.client.delete(f'{self.url}{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

