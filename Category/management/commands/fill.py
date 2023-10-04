from django.core.management import BaseCommand

from Category.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Кошка', 'description': 'Белая'},
            {'name': 'Медведь', 'description': 'Бурый'},
            {'name': 'Рысь', 'description': 'Какая то'},
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)

