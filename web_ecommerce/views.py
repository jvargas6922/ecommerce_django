from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.filter(sale=False)
    context ={'products': products}
    return render(request, 'product/index.html', context)

def create(request):
    return render(request, 'product/create.html')

@login_required
def sale(request):
    products = Product.objects.filter(sale=True)
    context ={'products': products}
    return render(request, 'product/sale.html', context)
