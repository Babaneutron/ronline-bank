# Generated by Django 2.2 on 2023-11-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20231125_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='address',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='card',
            name='phone',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
