from django.urls import path
#import path from urls.py main
from home import views
#import views.py from home folder

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    
    path('prediction/', views.prediction, name='prediction'),
    path('prediction', views.prediction, name='prediction'),
    
    path('contact/', views.contact, name='contact'),
      
    
    #when in url nothing comes it will be on home page and if about is added in url then it will be redirected to about page


]

'''
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
    Here first we have imported views and then we have to go to 
    views.index function in views.py file
    '''
