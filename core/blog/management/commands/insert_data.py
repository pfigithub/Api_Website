from django.core.management.base import BaseCommand

from faker import Faker
from datetime import datetime
import random

from accounts.models import User, Profile
from blog.models import Post, Category

# example for list of category
category_list = ["it", "iot", "python", "web", "hack"]


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="test@123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(6):
            Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                # image = "media/picture_name.format",
                content= self.fake.paragraph(nb_sentences=8),
                status= random.choice([True,False]),
                category= Category.objects.get(name=random.choice(category_list)),
                published_date= datetime.now(),
            )


# command for run:
            #  docker-compose exec backend sh -c "python manage.py insert_data(file_name)"
