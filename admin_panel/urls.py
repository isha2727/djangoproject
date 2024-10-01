
from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard,name="dashboard"),
    path('login/',views.login, name="login"),
    path('products/',views.products, name="products"),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product', views.edit_product, name="edit_product"),
    path('accounts/', views.accounts, name="accounts")
]