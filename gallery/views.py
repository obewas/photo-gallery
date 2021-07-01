from django.shortcuts import redirect, render
from .models import Image, Category
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import PhotoCreateForm
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

def create_photo(request):
    form = PhotoCreateForm(request.POST)
    if form.is_valid():
        label=form.cleaned_data['label']
        image = form.cleaned_data['image']
        description = form.cleaned_data['description']
        category = form.cleaned_data['category']
        location = form.cleaned_data['location']
        year_taken = form.cleaned_data['year_taken']
        form.save()
    else:
        form = PhotoCreateForm()

    return render(request, 'create_photo.html', {'form':form})

