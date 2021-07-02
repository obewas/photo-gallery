from django.shortcuts import redirect, render
from .models import Image, Category
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import PhotoCreateForm
from django.shortcuts import get_object_or_404
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
    form = PhotoCreateForm(request.POST, request.FILES)
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

def delete_photo(request, photo_id):
    photo = Image.objects.get(pk=photo_id)
    photo.delete()
    return redirect('/')

def update_photo(request, photo_id):
    photo = get_object_or_404(Image, pk=photo_id)
    if request.method == 'POST':
        form = PhotoCreateForm(request.POST, instance=photo)
        if form.is_valid():
        #label=form.cleaned_data['label']
        #image = form.cleaned_data['image']
        #description = form.cleaned_data['description']
        #category = form.cleaned_data['category']
       # location = form.cleaned_data['location']
        #year_taken = form.cleaned_data['year_taken']
            form.save()
            return redirect('/')
    else:
        form = PhotoCreateForm(instance=photo)
    return render(request, 'update_photo.html', {'form':form})

def get_photo_by_id(request, photo_id):
    photo = Image.objects.filter(pk=photo_id)
    context = {
        'photo':photo
    }
    return render(request, 'get_photo_by_id.html', context)

def search_photo(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        photo = Image.objects.filter(category=search)
        return render(request, 'search.html', {'photo':photo})