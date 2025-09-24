from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'blog/product_list.html',context={'products': products})







def product_detail(request,pk):
    detail = Product.objects.get(pk=pk)
    return render(request, 'blog/product_detail.html',context={'detail': detail})













