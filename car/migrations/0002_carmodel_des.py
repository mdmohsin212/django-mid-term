# Generated by Django 5.1.3 on 2024-11-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='des',
            field=models.TextField(default=None),
        ),
    ]
