# Generated by Django 2.0.5 on 2018-06-21 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conciergerie', '0003_auto_20180621_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
