from django.shortcuts import render
from product.models import Banner,Product

def home(request):
    banner = Banner.objects.all()
    products = Product.objects.all()
    data = {
        'banners':banner,
        'products':products,
    }
    return render(request,"home.html",data)

def about(request):
    return render(request,"home.html")
