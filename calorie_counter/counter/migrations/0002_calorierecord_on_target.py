# Generated by Django 3.0.2 on 2020-01-12 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calorierecord',
            name='on_target',
            field=models.BooleanField(default=True),
        ),
    ]
