"""restwithviewsets1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #,include
from testapp import views as v1
#from rest_framework import routers
from rest_framework.authtoken import views as v2
#router=routers.DefaultRouter()
#router.register('api',views.EmployeeCURDCBV)
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include(router.urls)),

    path("api/",v1.EmployeeListApiView.as_view()),
    path('get-api-token',v2.obtain_auth_token,name='get-api-token'),

]
