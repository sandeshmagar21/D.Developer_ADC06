# Generated by Django 2.1.7 on 2020-01-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='gym',
            name='workoutdesc',
            field=models.TextField(default=''),
        ),
    ]
