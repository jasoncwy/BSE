# Generated by Django 2.0 on 2017-12-27 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0006_auto_20171227_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('exchange', 'Exchange')], default='buy', max_length=20),
        ),
    ]