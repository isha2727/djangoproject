from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'admin_panel/index.html')

def login(request):
    return render(request, 'admin_panel/login.html')

def  products(request):
    return render(request, 'admin_panel/products.html')

def add_product(request):
    return render(request, 'admin_panel/add_product.html')

def edit_product(request):
    return render(request, 'admin_panel/edit_product.html')

def accounts(request):
    return render(request,'admin_panel/accounts.html')