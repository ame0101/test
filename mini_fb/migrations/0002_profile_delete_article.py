# Generated by Django 5.1.1 on 2024-10-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mini_fb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("email_address", models.EmailField(max_length=200)),
                ("profile_image_url", models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name="Article",
        ),
    ]
