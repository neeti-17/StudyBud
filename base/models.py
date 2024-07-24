from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
#  a topic can have multiple rooms but a room can have only one topic

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topic, on_delete= models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null =True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

# auto now take ss everytime we save the data
# auto now add takes only timestamp
    
# users can have different messages while a msg can have only one user 
# so its a one to many relationship from user -> to msg.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    # returns only first 50 characters


# django by default have sessions based authetication
# so when an user logs in the django administration it creates a session token in the database(settings.py > installed apps > sessions)
# this session token stores information like when the user logged in , who this user is , etc.
# go to django administration > inspect > application > session > cookies 

