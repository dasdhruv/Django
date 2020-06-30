# Lets set up the settings for this Script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


import random
from first_app.models import Users
from faker import Faker

fake_gen = Faker()
def poulate(n = 5):
    for i in range(n):
        name = fake_gen.name()
        last_name = fake_gen.last_name()
        email = fake_gen.email()

        u = Users.objects.get_or_create(user_name = name, user_lastname = last_name, user_email = email)[0]



if __name__ == '__main__':
    print("Populating Records....")
    poulate(20)
    print("Populating Completed")
