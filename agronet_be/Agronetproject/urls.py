from django.contrib import admin
from django.urls import path
from AgronetApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('orderDetail', views.OrderDetailView.as_view()),
    path('order', views.OrdersView.as_view()),
    path('product', views.ProductsView.as_view()),
   
]
