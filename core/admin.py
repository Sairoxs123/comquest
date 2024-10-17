from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Registration)

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["school", "number", "teacher_contact", "details"]
    ordering = ["number"]