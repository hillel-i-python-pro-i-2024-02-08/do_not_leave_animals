# Generated by Django 5.0.6 on 2024-07-09 18:08

import apps.animals_crm.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals_crm', '0002_alter_animalcard_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalcard',
            name='name',
            field=models.CharField(max_length=100, validators=[apps.animals_crm.models.ensure_required_case, apps.animals_crm.models.validate_not_use_underscore]),
        ),
    ]