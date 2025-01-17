# Generated by Django 5.1.3 on 2024-11-28 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0004_alter_brandmodel_slug'),
        ('car', '0009_remove_carmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brand.brandmodel'),
        ),
    ]
