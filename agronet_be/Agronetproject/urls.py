from django.contrib import admin
from django.urls import path
from AgronetApp import views
from AgronetApp.views.orderDetailView import OrderDetailDetail, OrderDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)



urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('orderDetail/', OrderDetailView.as_view()),
    path('orderDetail/{id}', OrderDetailDetail.as_view()),
    path('order/', views.OrdersView.as_view()),
    path('order/<int:pk>',views.OrdersDetail.as_view())
    path('product/',views.ProductCreateView.as_view()),
    path('product/<int:pk>',views.ProductDetailView.as_view()),
    path('city/',views.CityViews.as_view()),
    path('departament/',views.DepartamentView.as_view()),
]
