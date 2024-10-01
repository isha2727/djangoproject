from django.urls import path
from . import views

urlpatterns = [
    path('products/',views.allprod,name='getproducts'),
    path('product-details/<int:id>/',views.productDetail,name='productdetail'),
    path('add-product/',views.addProduct,name='add_product'),
    path('store-product/',views.storeProduct,name='store_product')
]