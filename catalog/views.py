#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from forms import ProductForm
from django.shortcuts import render,get_object_or_404

from models import Category,Product

# def redict(request):
#     # 1.实例化表单对象
#     publisher_form = ProductForm(request.POST)
#     return render(request, 'catalog/add_publisher2.html', locals())


def add_publisher(request):
    #1.实例化表单对象
    publisher_form = ProductForm(request.POST)
    if publisher_form.is_valid():
        publisher_form.save()
        print publisher_form
        return HttpResponse('添加商品信息成功')
    else:
        publisher_form = ProductForm()
        print  'is not ok data'
    return render(request,'catalog/add_publisher.html',locals())

def index(request):
    page_title ='产品分页目录－小白购'
    request.session['name'] = 'hello'
    return render(request,'catalog/index.html',locals())

def show_category_slug(request,category_slug):
    c = get_object_or_404(Category,slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request,'catalog/catalog.html',locals())
def show_product(request,product_slug):
    p = get_object_or_404(Product,slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    print request.session.get('name')
    return render(request, 'catalog/product.html', locals())



def show_product(request,product_slug):
    pass