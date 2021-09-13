from django.core.management import BaseCommand

from custom_user.models import CustomUser


class Command(BaseCommand):
    """
    Delete all users.
    """

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully'))
