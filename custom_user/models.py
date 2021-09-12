import uuid

from django.db import models


class CustomUser(models.Model):
    """
    User model.
    """
    id = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False, primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Name')
    last_name = models.CharField(max_length=255, verbose_name='Surname')
    email = models.EmailField(verbose_name='email address', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_transactions(self):
        return self.transaction_set.all()
