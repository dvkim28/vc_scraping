from django.db import models

from .utils import from_cyrillic_to_eng

def default_urls():
    return {"work": "", "jooble": ""}



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
        verbose_name = ('Vacancy ')
        verbose_name_plural = ('Vacancies')

    def __str__(self):
        return self.title

class Error(models.Model):
    timestamp = models.DateTimeField
    data = models.JSONField()

class Url(models.Model):
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
    url_data = models.JSONField(default=default_urls)

    class Meta:
        unique_together = ("city", "language")