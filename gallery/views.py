from django.shortcuts import render
from .models import Image, Category
# Create your views here.
def photo_list(request):
    photos = Image.objects.all()
    context = {
        'photos':photos
    }
    return render(request, 'photo_list.html', context)