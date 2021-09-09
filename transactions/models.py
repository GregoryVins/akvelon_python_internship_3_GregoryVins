import uuid

from django.db import models


class Transaction(models.Model):
    """
    Transactions model.
    """
    id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, primary_key=True)
    user = models.ForeignKey('custom_user.CustomUser', verbose_name='sender', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, verbose_name='the sum of a transaction')
    date = models.DateField(verbose_name='transaction date', auto_now_add=True)

    def __str__(self):
        return f'{self.amount} {self.user}'

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
