from django.db import models
from .harajatturi import Harajatturi

class Xarajat(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    xarajat_turi = models.ForeignKey('Harajatturi', on_delete=models.SET_NULL, null=True)
    oluvchi = models.CharField(max_length=50)
    cost = models.FloatField()


    def __str__(self):
        return self.name
