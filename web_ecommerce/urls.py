from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index_product'),
    path('create/', views.create, name='create_product'),
    path('sale/', views.sale, name='sale_product'),
]