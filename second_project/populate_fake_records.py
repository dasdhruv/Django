# Lets set up the settings for this Script
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()


import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

topics = ['Search','Social','Marketplace','News', 'Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

fake_gen = Faker()
def poulate(n = 5):
    for i in range(n):
        topics = add_topics()
        fname = fake_gen.company()
        furl = fake_gen.url()
        fdate = fake_gen.date()

        w_page = Webpage.objects.get_or_create(topic = topics, name = fname, url = furl)[0]
        a_record = AccessRecord.objects.get_or_create(name_webpage = w_page, date = fdate)[0]


if __name__ == '__main__':
    print("Populating Records....")
    poulate(20)
    print("Populating Completed")
