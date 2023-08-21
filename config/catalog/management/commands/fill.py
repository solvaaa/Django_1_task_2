from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_names = ["Смартфоны", "Ноутбуки", "Аксессуары"]
        category_descriptions = [
            "Электроника и девайсы: смартфоны",
            "Электроника и девайсы: ноутбуки",
            "Аксессуары для девайсов"
        ]
        category_length = len(category_names)
        for category in zip(range(1, category_length + 1), category_names, category_descriptions):
            Category.objects.create(pk=category[0], name=category[1], description=category[2])

        products = [
              {
                "pk": 1,
                "name": "IPhone 13",
                "description": "Смартфон от Apple, iPhone  13, OS X",
                "preview": "iphone13.jpg",
                "category": Category.objects.get(pk=1),
                "price": 100000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 2,
                "name": "Xiaomi 11T Pro",
                "description": "Смартфон от Xiaomi, Android",
                "preview": "xiaomi_11t.png",
                "category": Category.objects.get(pk=1),
                "price": 30000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 3,
                "name": "Samsung Galaxy A8",
                "description": "Смартфон от Samsung, Android",
                "preview": "galaxya8.jpg",
                "category": Category.objects.get(pk=1),
                "price": 40000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 4,
                "name": "Lenovo Ideapad",
                "description": "Ноутбук от Lenovo. 8 часов автономной работы. ОС Windows 11",
                "preview": "lenovo_ideapad.jpg",
                "category": Category.objects.get(pk=2),
                "price": 80000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 5,
                "name": "Huawei MateBook",
                "description": "Ноутбук от Huawei. 16 Gb RAM. ОС Windows 10",
                "preview": "huawei_matebook.jpg",
                "category": Category.objects.get(pk=2),
                "price": 60000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 6,
                "name": "Apple MacBook Air",
                "description": "Ноутбук от Apple. SSD: 256 Gb. ОС MacOS",
                "preview": "apple_macbook.jpg",
                "category": Category.objects.get(pk=2),
                "price": 100000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 7,
                "name": "Чехол для iPhone 13",
                "description": "Чехол с котиками",
                "preview": "iphone_case.jpg",
                "category": Category.objects.get(pk=3),
                "price": 1200,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 8,
                "name": "Стекло защитное для Xiaomi 11T Pro",
                "description": "Стекло для защиты экрана",
                "preview": "xiaomi_11t_glass.jpg",
                "category": Category.objects.get(pk=3),
                "price": 500,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              },
              {
                "pk": 9,
                "name": "Подставка охладительная для ноутбука",
                "description": "Подставка для охлаждения ноутбука",
                "preview": "laptop_cooler.jpg",
                "category": Category.objects.get(pk=3),
                "price": 5000,
                "date_created": "2023-08-21",
                "date_modified": "2023-08-21"
              }
        ]

        for product in products:
            Product.objects.create(**product)