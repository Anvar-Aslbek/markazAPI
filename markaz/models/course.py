from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices


class Course(models.Model):
    name = models.CharField(max_length=60)
    STATUS = Choices('30 daqiqa','40 daqiqa','60 daqiqa','90 daqiqa','120 daqiqa','180 daqiqa','240 daqiqa','280 daqiqa','300 daqiqa')
    course_duration = StatusField()
    cost = models.FloatField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.name


    