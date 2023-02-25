# Generated by Django 4.1.4 on 2023-02-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_category_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]