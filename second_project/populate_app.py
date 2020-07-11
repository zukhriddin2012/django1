import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

import random
from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_full_name = fakegen.name().split()
        fake_first_name = fake_full_name[0]
        fake_second_name = fake_full_name[1]
        fake_email = fakegen.email()
        print(fake_second_name)

        user_rec = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_second_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populating")
    populate()
    print("complete")
