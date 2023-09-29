import codecs
import os, sys
from django.db import DatabaseError


proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append('proj')
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service'
import django
django.setup()

from scraping.parsers import *
from scraping.models import City, Vacancy

parsers = ((work,'https://www.work.ua/jobs-python/'),
           (jooble,'https://ua.jooble.org/SearchResult?ukw=python'),
           )

city = City.objects.filter(slug='kyiv')
language = City.objects.filter(slug='python')


errors, jobs = [], []
for func, url in parsers:
    e, j = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
