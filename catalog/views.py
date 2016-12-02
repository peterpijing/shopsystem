#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from forms import ProductForm

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