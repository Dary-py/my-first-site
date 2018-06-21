from django.contrib import admin
from django.urls import path
from . import views, models
from django.conf import settings
from django.urls.converters import register_converter
from django.conf.urls.static import static
from django.views.generic import View, TemplateView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name = "main" ),
    path('about/', views.about_page, name = "about" ),
    path('menue/', views.menu_page, name = "menue" ),
     path('news/', views.news_page, name = "news" ),
     path('contact/', views.contacts_page, name = "contacts" ),
     path('single/', views.single_page, name = "single" ),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)