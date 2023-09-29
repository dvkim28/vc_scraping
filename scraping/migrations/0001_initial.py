# Generated by Django 4.2.5 on 2023-09-27 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'City name',
                'verbose_name_plural': 'Cities name',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Programming language ',
                'verbose_name_plural': 'Programming languages',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=256, verbose_name='Vacancy title')),
                ('company', models.CharField(max_length=256, verbose_name='Company name')),
                ('description', models.TextField(verbose_name='Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.city', verbose_name='City')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraping.language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Vacancy ',
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
