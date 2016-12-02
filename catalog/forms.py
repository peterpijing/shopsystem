#coding=utf-8
from django import forms
from models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("id","categories",)
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('价格必须大于0')
        return self.cleaned_data['price']

    # def clean(self):
    #     clean_data = super(ProductForm,self).clean()
    #     value = clean_data.get('name')
    #     try:
    #         ProductForm.objects.get(name=value)
    #         print '信息已经存在'
    #         #错误没有抛出？？？？why
    #         self._errors['name'] =self.error_class([u"%s的信息已经存在" % value])
    #     except ProductForm.DoesNotExist:
    #         pass
    #     return clean_data

#2.将默认label显示姓名－－》改为显示名称
    name = forms.CharField(label="名称")

