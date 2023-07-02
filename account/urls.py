from django.contrib import admin
from django.urls import path
from account import views


urlpatterns = [
    
    path('index',views.index,name="index"),
    path('user',views.user_register,name="userRegister"),
    path('seller',views.seller_register,name="sellerRegister"),
    path('login',views.login,name='login')

]
