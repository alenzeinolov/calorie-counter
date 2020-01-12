# Generated by Django 3.0.2 on 2020-01-12 05:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalorieRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('calories', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='calories')),
                ('comment', models.TextField(blank=True, default='', verbose_name='comment')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='records', related_query_name='record', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'calorie record',
                'verbose_name_plural': 'calorie records',
            },
        ),
    ]