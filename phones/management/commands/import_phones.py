import csv
from django.utils.text import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                phone_item = Phone()
                phone_item.id = line[0]
                phone_item.name = line[1]
                phone_item.image = line[2]
                phone_item.price = line[3]
                phone_item.release_date = line[4]
                phone_item.lte_exists = line[5]
                phone_item.slug = slugify(line[1])
                phone_item.save()
