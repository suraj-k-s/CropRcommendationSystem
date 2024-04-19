# Generated by Django 5.0.3 on 2024-03-22 01:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Adminstrator", "0012_delete_tbl_shopregistration"),
        ("Guest", "0015_tbl_newuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tbl_shopregistration",
            name="place",
        ),
        migrations.CreateModel(
            name="tbl_officer",
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
                ("officer_name", models.CharField(max_length=50)),
                ("officer_contact", models.CharField(max_length=50)),
                ("officer_email", models.CharField(max_length=50)),
                ("officer_password", models.CharField(max_length=50)),
                ("officer_address", models.CharField(max_length=50)),
                ("officer_photo", models.FileField(upload_to="Assets/officerPhoto/")),
                ("officer_proof", models.FileField(upload_to="Assets/officerProof/")),
                ("officer_status", models.IntegerField(default="0")),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Adminstrator.tbl_place",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="tbl_professor",
        ),
        migrations.DeleteModel(
            name="tbl_shopregistration",
        ),
    ]