# Generated by Django 3.2.8 on 2022-05-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]