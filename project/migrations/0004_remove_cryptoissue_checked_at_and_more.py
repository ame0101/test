# Generated by Django 5.1.1 on 2024-12-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_alter_cryptoissue_issue_hash"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cryptoissue",
            name="checked_at",
        ),
        migrations.AlterField(
            model_name="cryptoissue",
            name="code_snippet",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="cryptoissue",
            name="recommendation",
            field=models.TextField(blank=True, default=""),
        ),
    ]
