# Generated by Django 5.0.3 on 2024-03-22 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Adminstrator", "0012_delete_tbl_shopregistration"),
        ("Guest", "0016_remove_tbl_shopregistration_place_tbl_officer_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="tbl_professor",
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
                ("professor_name", models.CharField(max_length=50)),
                ("professor_contact", models.CharField(max_length=50)),
                ("professor_email", models.CharField(max_length=50)),
                ("professor_password", models.CharField(max_length=50)),
                ("professor_address", models.CharField(max_length=50)),
                ("professor_photo", models.FileField(upload_to="Assets/ProfPhoto/")),
                ("professor_proof", models.FileField(upload_to="Assets/ProfProof/")),
                ("professor_status", models.IntegerField(default="0")),
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
