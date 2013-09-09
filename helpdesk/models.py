from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (1, 'Not Started'),
    (2, 'Open'),
    (3, 'Finnished'),
    (4, 'Awaiting Requester'),
    (5, 'Awaiting Other Department'),
    (6, 'Awaiting Other'),
)

PRIORITY_CHOICES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Medium'),
    (4, 'Low'),
    (5, 'Unimportant'),
)

class Incident(models.Model):
    service_category = models.ForeignKey('ServiceCategory')
    status = models.PositiveSmallIntegerField(('status'), choices=STATUS_CHOICES, blank=False, null=False)
    priority = models.PositiveSmallIntegerField(('priority'), choices=PRIORITY_CHOICES, blank=False, null=False)
    #department = models.ForeignKey()#TODO: use django grops
    #technician = models.ForeignKey()#TODO: use django users

    #TODO: use django users, and
    requester = models.OneToOneField(User)
    #phone = models.ForeignKey()
    #mail = models.OneToOneField()
    #department = models.ForeignKey()

    incident_location = models.ForeignKey('IncidentLocation')
    category = models.ForeignKey('Category')
    subcategory = models.ForeignKey('SubCategory')

    subject = models.CharField(max_length=128)
    description = models.TextField()

    #history
    #checklist

class ServiceCategory(models.Model):
    name = models.CharField(max_length=128)

class IncidentLocation(models.Model):
    name = models.CharField(max_length=128)

class Category(models.Model):
    name = models.CharField(max_length=128)

class SubCategory(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey('Category')