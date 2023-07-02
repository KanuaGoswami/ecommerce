from django.shortcuts import render
from product.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all().values()
    print(products)
    return render(request,'home/index.html',{'products':products})