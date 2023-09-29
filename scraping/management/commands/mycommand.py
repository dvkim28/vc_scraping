from django.core.management import BaseCommand

from scraping.models import City, Vacancy, Language
from scraping.parsers import work, jooble

class Command(BaseCommand):
    def handle(self, *args, **options):
        parsers = ((work, 'https://www.work.ua/jobs-python/'),
                   (jooble, 'https://ua.jooble.org/SearchResult?ukw=python'),
                   )

        city = City.objects.filter(slug='kyiv').first()
        language = Language.objects.filter(slug='Python').first()

        errors, jobs = [], []
        for func, url in parsers:
            e, j = func(url)
            jobs += j
            errors += e

        for job in jobs:
            try:
                obj = Vacancy.objects.get(url=job['url'])
            except Vacancy.DoesNotExist:
                obj = Vacancy(**job, city=city, language=language)
                obj.save()