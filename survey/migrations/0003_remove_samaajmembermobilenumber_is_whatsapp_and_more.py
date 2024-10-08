# Generated by Django 4.2 on 2024-09-08 14:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import survey.validators


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0002_alter_samaajmembermobilenumber_mobile_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="samaajmembermobilenumber",
            name="is_whatsapp",
        ),
        migrations.AlterField(
            model_name="samaajmemberemail",
            name="email_address",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="samaajmembermobilenumber",
            name="mobile_number",
            field=models.CharField(
                max_length=10,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_numric_value",
                        message="Only digits are allowed in mobile number",
                        regex="^[0-9]*$",
                    ),
                    survey.validators.validate_mobile_number_length,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="samaajmembermobilenumber",
            name="samaaj_member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="survey.samaajmember"
            ),
        ),
    ]
