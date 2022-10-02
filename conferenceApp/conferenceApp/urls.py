"""conferenceApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('organizing_commitee/', views.organizing_commitee, name = 'organizing_commitee'),
    path('speakers/', views.speakers, name = 'speakers'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('venue/', views.venue, name = 'venue'),
    path('admin/', admin.site.urls),
    
    
]
