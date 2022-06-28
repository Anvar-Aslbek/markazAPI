from django.db import models
from django.contrib.auth.models import AbstractUser
from model_utils.fields import StatusField
from model_utils import Choices

##################
from .roll import Roll


class Employee(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    STATUS = Choices('Male','Female')
    gender = StatusField(blank=True, null=True)
    image = models.ImageField(upload_to='xodim/',null=True,blank=True)
    roll = models.ForeignKey('Roll',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = "Xodimlar"

