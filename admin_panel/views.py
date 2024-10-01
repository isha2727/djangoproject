from django.shortcuts import render
from django.http  import HttpResponse

from product.models import Product
# Create your views here.
def admin(request):
    return render(request, 'admin_panel/index.html')

def dashboard(request):
    return render(request, 'admin_panel/index.html')

def login(request):
    return render(request, 'admin_panel/login.html')

def  products(request):
    products=Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'admin_panel/products.html')

def addproduct(request):
    return render(request, 'admin_panel/add_product.html')

def edit_product(request):
    return render(request, 'admin_panel/edit-product.html')

def accounts(request):
    return render(request,'admin_panel/accounts.html')