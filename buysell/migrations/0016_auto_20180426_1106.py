# Generated by Django 2.0 on 2018-04-26 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0015_recommender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommender',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='recommender',
            name='quantity',
        ),
    ]
