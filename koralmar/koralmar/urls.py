"""
URL configuration for koralmar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('events/', views.events, name='events'),
    path('solfege/', views.solfege, name='solfege'),
    path('choir/', views.choir, name='choir'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('error404/', views.error404, name='error404'),
    path('surveys/', views.surveys, name='surveys'),
    path('mlts/', views.get_music_theory_lessons, name='get-mlts'),
    # path('get-photo/<int:id>/', views.get_photo, name='get-photo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
