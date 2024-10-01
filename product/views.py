from django.shortcuts import render
from product.models import Product,Category
# Create your views here.
from django.http import HttpResponse

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

def addProduct(request):
    return render(request,"add_product.html")

def storeProduct(request):
    if request.POST:

        form_data = str(request.POST.items)
        # print(form_data)
        # return HttpResponse("form data ", form_data)
        print(" ******** inserting form  ********")
        product_name = request.POST['pname']
        product_price =  request.POST['price']
        product_category =  request.POST['category']
        form_image = request.FILES['product_image']
        print(form_image)
        cat_obj = Category.objects.get(id=product_category)

        Product.objects.create(image=form_image,name=product_name,price=product_price,category=cat_obj)
        return HttpResponse(f"thanks product is added {product_name} Rs. {product_price}")