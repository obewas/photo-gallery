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
    path('search/', views.search_results, name='search'),
    path('location_filter', views.location_filter, name='location'),
    path('cats', views.cat, name='cats'),
    path('family', views.family, name='family'),
    path('travel', views.travel, name='travel'),
    path('sports', views.sports, name='sports'),
    path('landscape', views.landscape, name='landscape'),
    path('fashion', views.family, name='fashion'),
    



]