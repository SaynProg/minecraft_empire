# Generated by Django 4.1.3 on 2022-11-11 18:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0078_referenceindex'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(verbose_name='Кортокий Опис Сторінки')),
            ],
            options={
                'verbose_name': 'Сторінка Команди',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Ім'я")),
                ('detail_of_person', models.TextField(verbose_name='Опис Учасника')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Учасник Команди',
                'verbose_name_plural': 'Учасники Команди',
            },
        ),
    ]