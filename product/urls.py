from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.allprod, name='products'),
    path('products-details/<int:id>/',views.productDetail, name='productdetail'),
]