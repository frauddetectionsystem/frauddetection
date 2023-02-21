from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('productdetail/<int:pk>/', views.productdetail, name='productdetail'),
    path('pay/<int:pk>/', views.pay, name='pay'),
    path('confirm/<int:pk>',views.confirm, name='confirm'),
]