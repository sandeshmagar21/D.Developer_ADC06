# Generated by Django 3.0.1 on 2020-01-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workoutname', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('workoutdesc', models.TextField(default='Sachin Handsome')),
            ],
        ),
    ]
