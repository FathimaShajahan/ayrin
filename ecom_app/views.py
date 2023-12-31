# from django.http import  HttpResponse
# from django.shortcuts import get_object_or_404, render

# from . models import Category, Product

# # Create your views here.

# # def index(request):
# #     return HttpResponse("Hi hello welcome...")

# def allProCat(request,c_slug=None):
#     c_page=None
#     products=None
#     if c_slug is not None:
#         c_page = get_object_or_404(Category,slug = c_slug)
#         products = Product.objects.all().filter(category=c_page,available=True)
#     else:
#         products = Product.objects.all().filter(available=True)
#         return render(request,"category.html",{'category':c_page,'products':products})        

from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def allProCat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category = c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)
    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})


def proDetail(request,c_slug,product_slug):
    
    try:
        product = Product.objects.get(category__slug = c_slug,slug = product_slug)
    except Exception as e:
        raise e
    
    return render(request,'product.html',{'product':product})
