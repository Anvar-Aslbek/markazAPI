from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentAPIView.as_view()),
    path('detail/student/<int:pk>', StudentDetailAPIViews.as_view()),
    path('', StudentListApiView.as_view()),
    path('xodim/', EmployeeListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('day/', DayListApiView.as_view()),
    path('xarajat/', XarajatListApiView.as_view()),
    path('harajat-turi/', HarajatTuriListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    #############################################
    path('xodim/<int:pk>', EmployeeDetailAPIViews.as_view()),
    path('course/<int:pk>', CourseDetailAPIViews.as_view()),
    path('day/<int:pk>', DayDetailAPIViews.as_view()),
    path('xarajat/<int:pk>', XarajatDetailAPIViews.as_view())


]
