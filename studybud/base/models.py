from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name
    
class Room(models.Model):
  host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # OneToMany
  topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # OneToMany (a topic could has mutliple room, a room could only has one topic)
  name = models.CharField(max_length=200)
  description = models.TextField(null=True, blank=True) # null for database, blank for form
  # participants = 
  updated = models.DateTimeField(auto_now=True) # auto_now will take the timestep every time
  created = models.DateTimeField(auto_now_add=True) # auto_now_add for only the first time create this instance
  
  class Meta:
    ordering = ['-updated', '-created'] # show newest added item first
  def __str__(self):
    return self.name
  
class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)# OneToMany
  room = models.ForeignKey(Room, on_delete=models.CASCADE) # OneToMany, an Room could have multiple message, but message only belongs to one room.
  # models.SET_NULL: when the parent instance has been deleted, all the instance of the child will still in the database
  # Has to set null=True, since if the parent instance has been removed, this attribute could be null, null for database to be allowed
  # models.CASCADE: when the parent instance has been deleted, all the instance of the child will be deleted
  body = models.TextField()
  updated = models.DateTimeField(auto_now=True) # auto_now will take the timestep every time
  created = models.DateTimeField(auto_now_add=True) # auto_now_add for only the first time create this instance
  
  def __str__(self):
    return self.body[0:50] # only want the first 50 characters
  