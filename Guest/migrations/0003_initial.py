# Generated by Django 5.0.3 on 2024-03-14 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("Adminstrator", "0008_tbl_employee"),
        ("Guest", "0002_delete_tbl_newuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_newuser",
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
                ("Newuser_name", models.CharField(max_length=50)),
                ("Newuser_gender", models.CharField(max_length=50)),
                ("Newuser_contact", models.CharField(max_length=50)),
                ("Newuser_email", models.CharField(max_length=50)),
                ("Newuser_password", models.CharField(max_length=50)),
                ("Newuser_confirmpassword", models.CharField(max_length=50)),
                ("Newuser_dob", models.CharField(max_length=50)),
                ("Newuser_address", models.CharField(max_length=50)),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Adminstrator.tbl_place",
                    ),
                ),
            ],
        ),
    ]
