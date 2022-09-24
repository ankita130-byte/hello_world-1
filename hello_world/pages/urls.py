#pages/urls.py
#import path from django to power our URL pattern

from django.urls import path 

#import views. By reffering to the views.py file as .views we are telling django to look into the current directory for a views.py file and import the view homePageView

from .views import homePageView


urlpatterns = [
    path("", homePageView , name="home"),
]


#URL pattern has 3 parts
#a python regular expression for the empty string ""
#a reference too the view called homePageView
#an optional named URL patter called "home"