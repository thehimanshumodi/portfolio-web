# Generated by Django 5.1.3 on 2025-05-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=40)),
                ("content", models.TextField(max_length=400)),
                ("number", models.CharField(max_length=13)),
            ],
        ),
    ]
