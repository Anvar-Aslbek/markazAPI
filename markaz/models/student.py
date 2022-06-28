from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from model_utils.fields import StatusField
from model_utils import Choices
from .xodim import Employee

from .guruh import Group

class Student(Employee):
    bio = models.TextField(blank=True, null=True)
    guruh = models.ForeignKey('Group',on_delete=models.SET_NULL,null=True)
    come_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Student"