# Generated by Django 2.0.2 on 2019-04-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=12),
        ),
        migrations.AlterField(
            model_name='data',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=12),
        ),
    ]