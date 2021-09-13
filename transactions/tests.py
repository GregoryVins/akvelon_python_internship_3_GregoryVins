from django.test import TestCase
from rest_framework import status

from custom_user.models import CustomUser
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class TransactionTestCase(TestCase):
    def setUp(self):
        self.url = '/api/transactions/'
        self.user = CustomUser.objects.create(first_name='Test', last_name='Testov', email="test@example.local")
        self.transaction = Transaction.objects.create(user=self.user, amount=100)

    def test_get_transaction_list(self):
        """
        Successful request to transaction list
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transaction_detail(self):
        """
        Successful request to transaction detail
        """
        response = self.client.get(f'{self.url}{self.transaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TransactionSerializer(self.transaction).data)

    def test_create_transaction_success(self):
        """
        Successful creating of transaction
        """
        data = {
            "user": self.user.id,
            "amount": 100,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction_fail(self):
        """
        Failed creation of transaction
        """
        data = {
            "user": self.user
        }
        response = self.client.post(self.url, data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_transaction_success(self):
        """
        Successful transaction update
        """
        data = {
            "id": self.transaction.id,
            "user": self.transaction.user.id,
            "amount": 1111,
            "date": self.transaction.date
        }
        response = self.client.put(f'{self.url}{self.transaction.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_transaction_fail(self):
        """
        Failed transaction update
        """
        response = self.client.put(f'{self.url}{self.transaction.id}/', {}, content_type='application/json')
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_transaction(self):
        """
        Successful delete transaction
        """
        response = self.client.delete(f'{self.url}{self.transaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
