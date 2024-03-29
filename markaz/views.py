from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import *
from .models import *

from rest_framework import permissions


# Create your views here.


class EmployeeListApiView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = XodimSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = XodimSerializer(queryset, many=True)
        return Response(serializer.data)


class EmployeeDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = XodimSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = XodimSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListApiView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


class CourseDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = CourseSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = CourseSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DayListApiView(ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data)


class DayDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Day.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = DaySerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = DaySerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class XarajatListApiView(ListAPIView):
    queryset = Xarajat.objects.all()
    serializer_class = XarajatSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = XarajatSerializer(queryset, many=True)
        return Response(serializer.data)


class XarajatDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Xarajat.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = XarajatSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = XarajatSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HarajatTuriListApiView(ListAPIView):
    queryset = Harajatturi.objects.all()
    serializer_class = HarajatturiSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = HarajatturiSerializer(queryset, many=True)
        return Response(serializer.data)


class HarajatTuriDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Harajatturi.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = HarajatturiSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = HarajatturiSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IshHaqqiTuriListApiView(ListAPIView):
    queryset = IshHaqqiTuri.objects.all()
    serializer_class = IshHaqqiTuriSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = IshHaqqiTuriSerializer(queryset, many=True)
        return Response(serializer.data)


class IshHaqqiTuriDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return IshHaqqiTuri.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = IshHaqqiTuriSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = IshHaqqiTuriSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IshHaqqiListApiView(ListAPIView):
    queryset = IshHaqqi.objects.all()
    serializer_class = IshHaqqiSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = IshHaqqiSerializer(queryset, many=True)
        return Response(serializer.data)


class IshHaqqiDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return IshHaqqi.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = IshHaqqiSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = IshHaqqiSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentListApiView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)


class PaymentDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = PaymentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = PaymentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RollListApiView(ListAPIView):
    queryset = Roll.objects.all()
    serializer_class = RollSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RollSerializer(queryset, many=True)
        return Response(serializer.data)


class RollDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Roll.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = RollSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = RollSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoomListApiView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)


class RoomDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = RoomSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = RoomSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class XarajatListApiView(ListAPIView):
    queryset = Xarajat.objects.all()
    serializer_class = XarajatSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = XarajatSerializer(queryset, many=True)
        return Response(serializer.data)


class XarajatDetailAPIViews(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Xarajat.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = XarajatSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = XarajatSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
