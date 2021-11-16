from django.core.management.base import BaseCommand
from django.conf import settings
import json

from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        categories = load_from_json('categories')
        print(categories)

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')
        print(products)
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            category_item = ProductCategory.objects.get(name=category_name)
            product['category'] = category_item
            Product.objects.create(**product)