# Generated by Django 5.0.3 on 2024-03-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="date_released",
            field=models.DateField(),
        ),
    ]
