# Generated by Django 3.2.5 on 2021-08-01 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location')),
            ],
        ),
    ]
