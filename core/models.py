from django.db import models

# Create your models here.

class Registration(models.Model):
    school = models.CharField("School", max_length=100, unique=True)
    number = models.IntegerField("Number of events", blank=False)
    teacher_name = models.CharField("Teacher Name", max_length=100)
    teacher_mobile = models.CharField("Teacher Mobile", max_length=10)
    teacher_email = models.EmailField("Teacher Email", max_length=100)
    details = models.CharField("Details", max_length=3000, blank=False)
