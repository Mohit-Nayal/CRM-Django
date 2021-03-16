from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer-profile/<str:pk>', views.customer, name="customer"),  #dynamic url
    path('status/', views.status),

]