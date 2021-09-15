from django.core.management import BaseCommand

from transactions.models import Transaction


class Command(BaseCommand):
    """
    Delete all transactions.
    """

    def handle(self, *args, **options):
        Transaction.objects.all().delete()
