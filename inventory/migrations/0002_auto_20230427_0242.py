# Generated by Django 2.2.12 on 2023-04-27 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('CUP', 'Cup'), ('OZS', 'Ounce'), ('TBS', 'Tablespoon'), ('TSP', 'Teaspoon'), ('BOX', 'Box')], max_length=3),
        ),
    ]
