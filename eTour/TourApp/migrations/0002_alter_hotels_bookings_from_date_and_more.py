# Generated by Django 4.0.4 on 2022-07-08 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TourApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels_bookings',
            name='from_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='hotels_bookings',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.activate),
        ),
    ]
