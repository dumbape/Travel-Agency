# Generated by Django 2.1.7 on 2019-04-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_hotelbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='area',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
