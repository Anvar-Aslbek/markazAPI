from django.urls import path
from .views import *

urlpatterns = [
    path('xodim/', EmployeeListApiView.as_view()),
    path('course/', CourseListApiView.as_view()),
    path('day/', DayListApiView.as_view()),
    path('xarajat/', XarajatListApiView.as_view()),
    path('harajat-turi/', HarajatTuriListApiView.as_view()),
    path('ish-haqqi-turi/', IshHaqqiTuriListApiView.as_view()),
    path('ish-haqqi/', IshHaqqiListApiView.as_view()),
    path('payment/', PaymentListApiView.as_view()),
    path('roll/', RollListApiView.as_view()),
    path('room/', RoomListApiView.as_view()),
    path('xarajat/', XarajatListApiView.as_view()),
    #############################################
    path('xodim/<int:pk>', EmployeeDetailAPIViews.as_view()),
    path('course/<int:pk>', CourseDetailAPIViews.as_view()),
    path('day/<int:pk>', DayDetailAPIViews.as_view()),
    path('xarajat/<int:pk>', XarajatDetailAPIViews.as_view()),
    path('harajat-turi/<int:pk>', HarajatTuriDetailAPIViews.as_view()),
    path('ish-haqqi-turi/<int:pk>', IshHaqqiTuriDetailAPIViews.as_view()),
    path('ish-haqqi/<int:pk>', IshHaqqiDetailAPIViews.as_view()),
    path('payment/<int:pk>', PaymentDetailAPIViews.as_view()),
    path('roll/<int:pk>', RollDetailAPIViews.as_view()),
    path('room/<int:pk>', RoomDetailAPIViews.as_view()),
    path('xarajat/<int:pk>', XarajatDetailAPIViews.as_view()),




]
