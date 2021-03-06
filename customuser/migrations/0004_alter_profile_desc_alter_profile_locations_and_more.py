# Generated by Django 4.0.4 on 2022-05-29 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_profile_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desc',
            field=models.CharField(default='na', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='locations',
            field=models.CharField(default='kolkata', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='CustomerAppointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appnts', models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
