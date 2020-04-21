from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return "Project: {}".format(self.name)


class List(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Manager() 
    project = models.ForeignKey(Project, null=True, related_name='lists', on_delete= models.CASCADE, default = None)

    def __str__(self):
        return "List: {}".format(self.name)


class Card(models.Model):
    objects = models.Manager() 
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, default = None)
    list = models.ForeignKey(List, null=True, related_name="cards", on_delete= models.CASCADE, default = None)
    story_points = models.IntegerField(null=True, blank=True, default = None)
    business_value = models.IntegerField(null=True, blank=True, default = None)
    owner = models.ForeignKey(User, null=True, on_delete= models.CASCADE, default = None)

    def __str__(self):
        return "Card: {}".format(self.title)

