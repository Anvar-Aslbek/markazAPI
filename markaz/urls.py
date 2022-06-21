from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentAPIView.as_view()),
    path('detail/student/<int:pk>', StudentDetailAPIViews.as_view())
]
