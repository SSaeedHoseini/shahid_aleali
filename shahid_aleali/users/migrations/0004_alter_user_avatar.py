# Generated by Django 4.2.8 on 2023-12-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_avatar_user_birthday_user_national_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.FileField(blank=True, null=True, upload_to="upload"),
        ),
    ]
