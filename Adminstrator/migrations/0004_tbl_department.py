# Generated by Django 5.0.3 on 2024-03-13 01:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Adminstrator", "0003_tbl_adminregistration"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_department",
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
                ("department_name", models.CharField(max_length=50)),
            ],
        ),
    ]
