# Generated by Django 3.2.3 on 2022-05-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_phnnumber',
            field=models.IntegerField(max_length=10),
        ),
    ]
