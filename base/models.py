from django.db import models 
from django.contrib.auth.models import AbstractUser

# Create your models here.
#  a topic can have multiple rooms but a room can have only one topic


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


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

#the - before updated and created puts them in descending order
# auto now take ss everytime we save the data
# auto now add takes only timestamp when we first save the db
#black is for form and null is for db



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
#CASCADE will delete all childs of the parents if parent is deleted

