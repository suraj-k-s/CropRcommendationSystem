# Generated by Django 5.0.4 on 2024-04-18 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_tbl_predictionhead_tbl_predictiondata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_predictionhead',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_predictionData',
        ),
        migrations.DeleteModel(
            name='tbl_predictionHead',
        ),
    ]