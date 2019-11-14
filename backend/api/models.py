from django.db import models
from rest_framework import serializers

# from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class User(AbstractUser):
    followers = ManyToManyField('self', related_name='followees', symmetrical=False)


class Post(Model):
    author = ForeignKey(User, related_name='posts', on_delete=CASCADE)

    created = DateTimeField(auto_now_add=True)
    content = TextField(blank=True, null=True)
    title = CharField(max_length=255)
    updated = DateTimeField(auto_now=True)


class Course(models.Model):
    members = ManyToManyField(User, related_name='members_list', blank=True)

    name = models.CharField(max_length=200)
    
    DIRECTION_STATUS = (
        ('h', 'html'),
        ('j', 'js'),
        ('p', 'php'),
        ('py', 'python'),
    )

    direction = models.CharField(max_length=2, choices=DIRECTION_STATUS, blank=True, default='py', help_text='Направление курса')
    date_start = models.DateField(null=True, blank=True)
    date_start_registration = models.DateField('Начало регистрации', null=True, blank=True)

    LEVEL_STATUS = (
        ('j', 'Junior'),
        ('m', 'Middle'),
        ('s', 'Senior'),
        ('l', 'Lead'),
    )

    level = models.CharField(max_length=1, choices=LEVEL_STATUS, blank=True, default='j', help_text='Уровень курса')
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, max_length=2000, help_text="Описание курса")

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

# class CourseParticipants(models.Model):
#     id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
#     id_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True) 

