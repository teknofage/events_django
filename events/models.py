from django.db import models


# Create your models here.

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)
    
def __str__(self):
    return self.name

class Person(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    