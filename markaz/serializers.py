from dataclasses import fields
from rest_framework import serializers
from .models import *

class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class HarajatturiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harajatturi
        fields = '__all__'

class IshHaqqiTuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshHaqqiTuri
        fields = '__all__'

class IshHaqqiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshHaqqi
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class XarajatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xarajat
        fields = '__all__'