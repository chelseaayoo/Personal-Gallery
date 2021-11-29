from django.conf.urls import url 
from .import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^today/$',views.gallery_of_day,name='galleryToday'),
    url(r'^photo/$',views.get_photo,name='photos'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)