from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

class EmployeeListApiView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    search_fields=('ename',)
# Create your views here.
#class EmployeeCURDCBV(ModelViewSet):
    #queryset=Employee.objects.all()
    #serializer_class=EmployeeSerializer