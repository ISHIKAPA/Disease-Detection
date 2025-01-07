"""
URL configuration for SleepPtterns project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #This path shows that when user types admin/ then our website gets to admin.site.urls
    path('',include('home.urls')),
    #Add all the other paths to include as mentioned above in point 3.2
   
#Yaha par agar ham admin me nhi jayenge toh wo hame bhej dega
#home.urls me 
#Phir further urls waha se honge



]
