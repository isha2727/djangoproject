from django.shortcuts import render
from product.models import Product
# Create your views here.
# def Product(request):
#     Product=Product.objects.all()
#     data={'title':"Daraz Ecom| product page dynamic title" , 'page_heading':"product"}
#     return render(request,"product.html" , data)

def allprod(request):
    all_products = Product.objects.all()
    data = {
        'products': all_products
    }
    return render(request,"products.html",data)

def productDetail(request,id):

    single_product = Product.objects.filter(id=id).first()
    data = {
        'product':single_product,
    }
    return render(request,"single_product.html",data)