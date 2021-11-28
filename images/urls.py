from django.conf.urls import url 
from .import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path


urlpatterns = [
    url(r'^search/', views.search, name='search_results'),
    url(r'^$',views.welcome,name='index'),
    url(r'^location/',views.location,name='location'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)