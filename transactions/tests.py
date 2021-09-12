from django.test import TestCase

from custom_user.models import CustomUser
from transactions.models import Transaction


class TransactionTestCase(TestCase):
    def setUp(self):
        self.url = '/api/transactions/'
        self.user = CustomUser.objects.create(first_name='Test', last_name='Testov', email="test@example.local")
        self.transaction = Transaction.objects.create(user=self.user, amount=100)

    def test_get_transaction_list(self):
        """"""

    def test_get_transaction_detail(self):
        """"""

    def test_create_transaction_success(self):
        """"""

    def test_create_transaction_fail(self):
        """"""

    def test_update_transaction_success(self):
        """"""

    def test_update_transaction_fail(self):
        """"""

    def test_delete_transaction(self):
        """"""
