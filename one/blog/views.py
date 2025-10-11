from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product_list.html',context={'products': products})


def product_detail(request,pk):
    detail = Product.objects.get(pk=pk)
    return render(request, 'blog/product_detail.html',context={'detail': detail})


def add_to_product(request):
    n = request.GET.get('title')
    d = request.GET.get('Description')
    p = request.GET.get("price")
    if n and d and p:
        Product.objects.create(title=n, Description=d, price=p,numberOfProduct=0)








    return render(request, 'blog/add_to_product.html')
