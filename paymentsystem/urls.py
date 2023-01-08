from django.urls import path
from . import views

app_name = 'paymentsystem'

urlpatterns = [
    path('', views.index, name='index')
]