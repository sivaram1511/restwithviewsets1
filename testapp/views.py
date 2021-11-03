from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

class EmployeeListApiView(ListAPIView):
    # queryset=Employee.objects.all()
    # serializer_class=EmployeeSerializer
    # print("get all Employee  records ")
    serializer_class=EmployeeSerializer
    def get_queryset(self):
        print("Searching operation")
        qs=Employee.objects.all()
        name=self.request.GET.get('ename')
        if name is not None:
            qs=qs.filter(ename__icontains=name)
        return qs
   print("get the name")     

# Create your views here.
#class EmployeeCURDCBV(ModelViewSet):
    #queryset=Employee.objects.all()
    #serializer_class=EmployeeSerializer