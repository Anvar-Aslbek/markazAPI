from django.db import models
from django.contrib.auth.models import User
from model_utils.fields import StatusField
from model_utils import Choices

##################
from .roll import Roll


class Employee(User):
    phone = models.CharField(max_length=15)
    birth_day = models.DateField()
    STATUS = Choices('Male','Female')
    gender = StatusField()
    image = models.ImageField(upload_to='xodim/',null=True,blank=True)
    roll = models.ForeignKey('Roll',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.first_name

