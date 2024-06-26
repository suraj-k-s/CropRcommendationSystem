# Generated by Django 5.0.3 on 2024-04-04 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Guest", "0019_tbl_user"),
        ("Officer", "0001_initial"),
        ("User", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_apply",
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
                ("request_date", models.DateField(auto_now_add=True)),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Officer.tbl_notification",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Guest.tbl_user"
                    ),
                ),
            ],
        ),
    ]
