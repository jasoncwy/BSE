# Generated by Django 2.0 on 2018-02-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0014_auto_20180209_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('productName', models.CharField(max_length=255)),
                ('sales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(max_length=255)),
                ('reviewRating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('clicks', models.IntegerField(max_length=255)),
                ('timeSpent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buysell.User_info')),
            ],
        ),
    ]