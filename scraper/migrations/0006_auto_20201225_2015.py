# Generated by Django 3.1.4 on 2020-12-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20201225_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebookposts',
            name='post_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
