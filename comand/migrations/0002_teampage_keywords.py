# Generated by Django 4.1.3 on 2022-11-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='keywords',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Ключові слова для пошуку'),
        ),
    ]