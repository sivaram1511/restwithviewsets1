from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

class EmployeeListApiView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    print("get all records")

# Create your views here.
#class EmployeeCURDCBV(ModelViewSet):
    #queryset=Employee.objects.all()
    #serializer_class=EmployeeSerializer