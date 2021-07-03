from django.db.models import query
from django.shortcuts import redirect, render
from .models import Image, Category
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import PhotoCreateForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .filters import ImageFilter
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


def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_articles = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location_filter(request):
    filter = ImageFilter(request.GET, queryset=Image.objects.all())
    return render(request, 'filter.html', {'filter': filter})


def sports(request):
    sports_category = Category.objects.get(pk=4)
    sports = Image.objects.all().filter(category=sports_category)
    return render(request,'category/sports.html', {'sports':sports})


def travel(request):
    travel_category = Category.objects.get(pk=1)
    travel = Image.objects.filter(category=travel_category)
    return render(request,'category/travel.html', {'travel':travel})


def fashion(request):
    fashion_category = Category.objects.get(pk=5)
    fashion = Image.objects.filter(category=fashion_category)
    return render(request,'category/fashion.html', {'fashion':fashion})

def family(request):
    family_category = Category.objects.get(pk=4)
    family = Image.objects.filter(category=family_category)
    return render(request,'category/family.html', {'family':family})

def landscape(request):
    landscape_category = Category.objects.get(pk=3)
    landscape = Image.objects.filter(category=landscape_category)
    return render(request, 'category/landscape.html', {'landscape':landscape})

def cat(request):
    cats = Category.objects.all()
    context = {
        'cats':cats
    }
    return render(request, 'cats.html', context)