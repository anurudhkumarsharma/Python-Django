"""textutils URL Configuration

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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.index,name='home'),
    path('analyze',views.analyze,name='analyze'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.aboutus,name='aboutus'),
    #path('feature',views.feature,name='feature'),
    #path('capitalizefirst',views.capfirst,name='capitalizefirst'),
    #path('newlineremove',views.newlineremove,name='capfirst'),
    #path('spaceremove',views.spaceremove,name='space remove'),
    #path('charcount',views.charcount,name='charcount'),
    

]
