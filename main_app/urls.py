# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.show),
    url(r'^post_url/$', views.post_auto, name='post_auto'),
]