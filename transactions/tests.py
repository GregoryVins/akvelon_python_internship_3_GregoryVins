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
        Request transaction list.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_transaction_detail(self):
        """
        Request transaction detail information.
        """
        response = self.client.get(f'{self.url}{self.transaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TransactionSerializer(self.transaction).data)

    def test_create_transaction_success(self):
        """
        Request to success create new transaction.
        """
        data = {
            'user': self.user.id,
            'amount': 1234
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_transaction_fail(self):
        """
        Request to fail create new transaction.
        """
        response = self.client.post(self.url, {})
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_transaction_success(self):
        """
        Successful edit transaction.
        """
        data = {
            'id': self.transaction.id,
            'user': self.transaction.user_id,
            'amount': 999,
            'date': self.transaction.date
        }
        response = self.client.put(f'{self.url}{self.transaction.id}/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_transaction_fail(self):
        """
        Successful edit transaction.
        """
        response = self.client.put(f'{self.url}{self.transaction}/', {})
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_transaction(self):
        """
        Successful delete transaction.
        """
        response = self.client.delete(f'{self.url}{self.transaction.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
