# Generated by Django 4.2.1 on 2023-05-12 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esicommodel",
            name="compound_name",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="esicommodel",
            name="smiles",
            field=models.CharField(max_length=500),
        ),
    ]
