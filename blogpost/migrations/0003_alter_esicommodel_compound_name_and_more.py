# Generated by Django 4.2.1 on 2023-05-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogpost", "0002_alter_esicommodel_compound_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="esicommodel", name="compound_name", field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="esicommodel", name="smiles", field=models.CharField(),
        ),
    ]
