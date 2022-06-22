from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from model_utils.fields import StatusField
from model_utils import Choices

from .guruh import Group

class Student(User):
    phone = models.CharField(max_length=20)
    birth_day = models.DateField()
    STATUS = Choices('Male','Female')
    gender = StatusField()
    bio = models.TextField()
    guruh = models.ForeignKey('Group',on_delete=models.SET_NULL,null=True)
    come_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Student"