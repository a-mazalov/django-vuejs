# Generated by Django 2.2.1 on 2019-11-30 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_user_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
    ]
