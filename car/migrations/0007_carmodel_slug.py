# Generated by Django 5.1.3 on 2024-11-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_carmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
