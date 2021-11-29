from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Category, Image, Location
from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def welcome(request):
    categories = Category.objects.all()
    try:
        photos = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request,'index.html',{'photos':photos,'categories':categories})

def gallery_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def get_photo(request):
    try:
        photos = Image.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    # import pdb; pdb.set_trace()
    return render(request, 'image.html', {"photos":photos})

def get_category(request):
    category = Category.object.all()

    return render(request,'index.html', {"category":category})
 
def search_results(request):
    if 'photo' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def get_location(request):
    location = Location.object.all()

    return render(request,'index.html', 'base.html','image.html','navbar.html',{"location":location})