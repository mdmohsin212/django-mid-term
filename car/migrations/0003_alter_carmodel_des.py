# Generated by Django 5.1.3 on 2024-11-28 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_carmodel_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='des',
            field=models.TextField(blank=True, null=True),
        ),
    ]