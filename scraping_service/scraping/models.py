from django.db import models

from .utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    slug = models.SlugField(
        max_length=128,
        unique=True,
        blank=True,
    )

    class Meta:
        app_label = 'scraping'
        verbose_name = ('City name')
        verbose_name_plural = ('Cities name')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
    )
    slug = models.SlugField(
        max_length=128,
        unique=True,
        blank=True,
    )

    class Meta:
        app_label = 'language'
        verbose_name = ('Programming language ')
        verbose_name_plural = ('Programming languages')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(
        unique=True,
    )
    title = models.CharField(
        max_length=256,
        verbose_name='Vacancy title'
    )
    company = models.CharField(
        max_length=256,
        verbose_name='Company name'
    )
    description = models.TextField(
        verbose_name='Description'
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        verbose_name='City'
    )
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        verbose_name='Language'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        app_label = 'scraping'
        verbose_name = ('Vacancy ')
        verbose_name_plural = ('Vacancies')

    def __str__(self):
        return self.title
