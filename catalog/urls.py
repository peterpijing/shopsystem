from django.conf.urls import url

from views import *


urlpatterns = [
    url(r'^add_publisher/$',add_publisher,name='add_publisher'),
    # url(r'^redict/$',redict,name='redict'),
]