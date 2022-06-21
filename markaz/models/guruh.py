from django.db import models

from .xodim import Employee
from .course import Course
from .day import Day
from .room import Room

class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True)
    days = models.ManyToManyField(Day)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    lesson_time = models.TimeField()
    beginning_date = models.DateField()

    def __str__(self):
        return self.name