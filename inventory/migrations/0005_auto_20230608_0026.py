# Generated by Django 2.2.12 on 2023-06-08 04:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20230605_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.1)]),
        ),
        migrations.AlterUniqueTogether(
            name='reciperequirement',
            unique_together={('menu_item', 'ingredient')},
        ),
    ]
