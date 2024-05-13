# Generated by Django 2.2 on 2023-10-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(blank=True, default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(blank=True, default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='air',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='home',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='job',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='location',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='phone',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sex',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type_event',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
