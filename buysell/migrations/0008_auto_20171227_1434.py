# Generated by Django 2.0 on 2017-12-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0007_auto_20171227_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('exchange', 'Exchange')], default='', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('exchange', 'Exchange')], max_length=20, unique=True),
        ),
    ]