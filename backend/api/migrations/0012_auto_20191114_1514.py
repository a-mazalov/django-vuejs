# Generated by Django 2.2.1 on 2019-11-14 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191114_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
