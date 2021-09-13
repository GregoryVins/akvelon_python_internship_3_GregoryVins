from random import choice, choices
from string import ascii_letters

from django.core.management import BaseCommand

from custom_user.models import CustomUser


class Command(BaseCommand):
    USER_COUNT = 10
    NAME_LENGTH = 10

    def create_random_name(self):
        """
        Create random name from random letters.
        :return: Sum of random letters.
        """
        name = ''
        for _ in range(self.NAME_LENGTH):
            name += choice(ascii_letters)
        return name

    def create_random_surname(self):
        """
        Create random surname from random letters.
        :return: Sum of random letters.
        """
        surname = ''
        for _ in range(self.NAME_LENGTH):
            surname += choice(ascii_letters)
        return surname

    def create_random_email(self):
        """
        Create random email from random letters.
        :return: email address.
        """
        email = ''
        for _ in range(self.NAME_LENGTH):
            email += choice(ascii_letters)
        email += '@example.local'
        return email

    def get_user_params(self):
        """
        Alternative way with single cycle.
        :return: 3 params: first_name, last_name, email
        """
        first_name = ''
        last_name = ''
        email = ''
        for _ in range(self.NAME_LENGTH):
            symbols = choices(ascii_letters, k=3)
            first_name += symbols[0]
            last_name += symbols[1]
            email += symbols[2]
        email += '@example.local'
        return first_name, last_name, email

    def handle(self, *args, **options):
        for j in range(self.USER_COUNT):
            first_name, last_name, email = self.get_user_params()
            CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email)
        self.stdout.write(self.style.SUCCESS('Successfully'))
