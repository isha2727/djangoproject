
from . import views
from django.urls import path

urlpatterns = [
    path('', views.admin,name="admin"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('login/',views.login, name="login"),
    path('products/',views.products, name="products"),
    path('add_product/', views.addproduct, name='product_add'),
    path('edit_product', views.edit_product, name="edit_product"),
    path('accounts/', views.accounts, name="accounts"),
]