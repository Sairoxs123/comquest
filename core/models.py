from django.db import models

# Create your models here.

class Registration(models.Model):
    school = models.CharField("School", max_length=100, unique=True)
    number = models.IntegerField("Number of events", blank=False)
    teacher_contact = models.CharField("Teacher Contact", max_length=10)
    details = models.CharField("Details", max_length=3000, blank=False)
