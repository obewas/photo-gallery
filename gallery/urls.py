from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    url(r'^photo/(\d+)',views.single_photo,name ='photo'),
    url(r'^create/$', views.create_photo, name='create'),
    url(r'^delete/(\d+)$', views.delete_photo, name='delete'),
    path('update/<int:photo_id>/', views.update_photo,name='update'),
    path('get_photo_by_id/<int:photo_id>',views.get_photo_by_id, name='get_photo_by_id'),
    path('search/', views.search_photo, name='search'),
]