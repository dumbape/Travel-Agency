# Generated by Django 2.1.7 on 2019-03-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMetaData',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('db_name', models.CharField(max_length=50)),
            ],
        ),
    ]