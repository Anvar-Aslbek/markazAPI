from django.db import models
from .course import Course
from .ish_haqqi_turi import IshHaqqiTuri

class IshHaqqi(models.Model):
    cource = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    miqdor = models.IntegerField()
    ish_haqqi_turi = models.ForeignKey('IshHaqqiTuri', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cource
