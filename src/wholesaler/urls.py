from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),  
    path('wholesaler/',views.wholesaler,name='wholesaler_dashboard'),   
    path('wholesaler/saree/',views.saree,name='saree'),
    path('logout/', views.logout_view, name='logout'),   
]