# Generated by Django 4.2 on 2023-10-31 05:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="samaajmembermobilenumber",
            name="mobile_number",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]