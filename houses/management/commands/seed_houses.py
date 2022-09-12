import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from houses import models as house_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates Houses"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many houses you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        house_types = house_models.RoomType.objects.all()
        seeder.add_entity(
            house_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "house_types": lambda x: random.choice(house_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} houses created!"))
