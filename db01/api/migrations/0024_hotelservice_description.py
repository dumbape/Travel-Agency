# Generated by Django 2.1.7 on 2019-04-13 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_hotelbooking_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelservice',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
