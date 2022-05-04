"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from customuser.views import CustomerSignUpView,SellerSignUpView,activate,loginUser,logout_user,profilepage,index,updateprofile

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/customersignup/', CustomerSignUpView, name='customer_signup'),
    path('accounts/sellersignup/', SellerSignUpView, name='seller_signup'),
    path('accounts/login/',loginUser, name='login'),
    path('accounts/logout/',logout_user, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'), 
    path('profile/',profilepage,name='profile'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('index/',index,name='index'),
]