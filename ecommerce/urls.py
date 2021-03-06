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

from customuser.views import details,look,CustomerSignUpView,Customer_Appoinment,SellerSignUpView,activate,loginUser,logout_user,profilepage,index,updateprofile,Custm_apnts,Seller_apnts
from customuser import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customersignup/', CustomerSignUpView, name='customer_signup'),
    path('sellersignup/', SellerSignUpView, name='seller_signup'),
    path('login/',loginUser, name='login'),
    path('logout/',logout_user, name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate, name='activate'), 
    path('profile/',profilepage,name='profile'),
    path('updateprofile/',updateprofile,name='updateprofile'),
    path('',index,name='index'),
    #path('home/',views.home, name="home"),
    path('details/<str:username>/',details,name="detail"),
    path('bookappointment/<str:username>/',Customer_Appoinment,name="Customer_Appoinment"),
    path('Customer_apnts/',Custm_apnts,name="Customer_Appoinment"),
    path('Seller_apnts/',Seller_apnts,name="Seller_Appoinment"),
    path('view/<str:username>/',look,name="look"),
]
