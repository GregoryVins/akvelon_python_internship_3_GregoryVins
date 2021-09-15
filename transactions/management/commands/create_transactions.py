from random import choice, randint

from django.core.management import BaseCommand

from custom_user.models import CustomUser
from transactions.models import Transaction


class Command(BaseCommand):
    """
    Generate random transactions.
    """

    TRANSACTION_COUNT = 50

    def handle(self, *args, **options):
        user_list = CustomUser.objects.all()
        for _ in range(self.TRANSACTION_COUNT):
            Transaction.objects.create(user=choice(user_list), amount=randint(-1000000, 1000000))
        self.stdout.write(self.style.SUCCESS('Successfully'))
