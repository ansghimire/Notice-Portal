# Generated by Django 4.1.4 on 2022-12-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads_image', models.ImageField(upload_to='ads-image/')),
                ('ads_type', models.CharField(choices=[('vertical', 'Vertical'), ('horizontal', 'Horizontal'), ('square', 'Square')], default='vertical', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('description2', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('slug', models.SlugField(max_length=240, unique=True)),
                ('exprity_date', models.DateTimeField()),
                ('file', models.FileField(upload_to='documents/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('cateogry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notice.category')),
            ],
        ),
    ]
