from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentAPIView.as_view()),
    path('detail/student/<int:pk>', StudentDetailAPIViews.as_view()),
    path('', StudentListApiView.as_view()),
    path('xodim/', EmployeeListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('day/', DayListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view())


]
