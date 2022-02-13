# Generated by Django 4.0 on 2022-01-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('podcast_url', models.URLField(max_length=1000, verbose_name='Podcast Url')),
                ('image_url', models.URLField(max_length=2000, verbose_name='Image Url')),
                ('authors', models.ManyToManyField(to='core.Author', verbose_name='Authors')),
                ('categories', models.ManyToManyField(to='core.Category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcasts',
            },
        ),
    ]
