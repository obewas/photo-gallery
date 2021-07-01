from django.shortcuts import render
from .models import Image, Category
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
# Create your views here.
def photo_list(request):
    photos = Image.objects.all()
    context = {
        'photos':photos
    }
    return render(request, 'photo_list.html', context)

def single_photo(request, photo_id):
    try:
       photo =  Image.objects.get(pk=photo_id)
    except:
        Image.DoesNotExist
        raise Http404()
    return render(request, 'photo.html', {'photo':photo})