from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    url(r'^photo/(\d+)',views.single_photo,name ='photo'),
    url(r'^create/$', views.create_photo, name='create'),
]