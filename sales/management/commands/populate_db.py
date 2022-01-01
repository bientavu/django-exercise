from datetime import date
from decimal import Decimal
from random import choice

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from sales.models import Article, ArticleCategory, Sale
from users.models import User

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with dummy data."

    @transaction.atomic
    def handle(self, *args, **options):
        users = [User.objects.create_user(email=fake.ascii_email()) for _ in range(10)]
        categories = ArticleCategory.objects.bulk_create(
            [ArticleCategory(display_name=fake.word()) for _ in range(10)]
        )
        articles = Article.objects.bulk_create(
            [
                Article(
                    code=fake.pystr(3, 3).upper() + str(fake.pyint(100, 999)),
                    category=choice(categories),
                    name=fake.word(),
                    manufacturing_cost=fake.pydecimal(
                        left_digits=3, right_digits=2, positive=True
                    ),
                )
                for _ in range(100)
            ]
        )
        sales = []
        for _ in range(1000):
            article = choice(articles)
            sales.append(
                Sale(
                    date=fake.date_between_dates(date(2021, 1, 1), date(2021, 12, 31)),
                    author=choice(users),
                    article=article,
                    quantity=fake.pyint(1, 99),
                    unit_selling_price=Decimal(fake.pyint(120, 150) / 100)
                    * article.manufacturing_cost,
                )
            )
        Sale.objects.bulk_create(sales)
