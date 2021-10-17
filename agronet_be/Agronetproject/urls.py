from django.contrib import admin
from django.urls import path
from AgronetApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('orderDetail', views.OrderDetailView.as_view()),
    path('order', views.OrdersView.as_view()),
    path('products/',views.ProductsView.as_view()),
    path('product/<int:id_product>',views.specificProductView.as_view())
]
