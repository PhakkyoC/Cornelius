# Generated by Django 2.0.5 on 2018-06-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conciergerie', '0002_place_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='nbvotes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
