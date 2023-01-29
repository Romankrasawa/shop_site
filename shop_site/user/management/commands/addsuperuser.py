from django.core.management.base import BaseCommand
from user.models import User

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        """
        Custom creating super user command 
        """
        username = input("Імя: ")
        last_name = input("Прізвище: ")
        email = input("Email: ")
        password = input("Пароль: ")
        pasword_repeat = input("Повторіть пароль: ")
        if password == pasword_repeat and all([username, last_name, email]):
            try:
                user = User.objects.create_superuser(
                        email=email,
                        username=username,
                        last_name=last_name,
                        password=password
                        )
                print("Користувач був успішно створений.")
            except Exception as error:
                print(f"Виникла помилка {error}")
        else:
            print("Некорекні дані")
