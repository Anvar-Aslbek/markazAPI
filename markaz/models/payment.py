from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices


from .student import Student


class Payment(models.Model):
    student = models.ForeignKey('Student',on_delete = models.SET_NULL,null=True)
    STATUS = Choices('Naqt pul','UZCARD','Bank hisobi')
    payment_method = StatusField()
    quantity = models.FloatField()
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.student