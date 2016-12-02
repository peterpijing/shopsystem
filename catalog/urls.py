from django.conf.urls import url

from views import *


urlpatterns = [
    url(r'^add_publisher/$',add_publisher,name='add_publisher'),
    # url(r'^redict/$',redict,name='redict'),
    url(r'^$',index,name='index'),
    url(r'^(?P<category_slug>[-\w]+)/$',show_category_slug,name='show_category_slug'),
    url(r'^(?P<product_slug>[-\w]+)/$',show_product,name='show_product'),
]
