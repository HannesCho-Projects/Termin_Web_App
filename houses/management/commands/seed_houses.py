import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
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
        house_type = house_models.HouseType.objects.all()
        seeder.add_entity(
            house_models.House,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "house_type": lambda x: random.choice(house_type),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        amenities = house_models.Amenity.objects.all()
        facilities = house_models.Facility.objects.all()
        rules = house_models.HouseRule.objects.all()
        for pk in created_clean:
            house = house_models.House.objects.get(pk=pk)
            for i in range(1, random.randint(3, 5)):
                house_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    house=house,
                    file=f"house_photos/{random.randint(1, 31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    house.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    house.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    house.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} houses created!"))
