from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()

urlpatterns = [
    #path for getting all school data
    path('index/', views.index.as_view(), name='index'),

    #path for getting all the users
    path('users', views.users.as_view()),

    #path for registering a user
    url('register/', views.RegisterView.as_view()),

    #Path for home
    url('home/', views.HomePageView.as_view()),
  
    #path for charts
    url('charts/', views.ChartsView.as_view()),

    #Path for signup
    url('login/', views.LoginView.as_view()),

    #Path for getting data from department
    path('single/<str:schoolName>/<str:departmentName>/', views.singleData.as_view(), name = 'singleData'),
    
    #Path for getting multiple departments from single school    
    path('multiple/<str:schoolName>/', views.multipleData.as_view(), name = 'multipleData'),
    
    #Path for uploading data
    path('upload/', views.uploadFile, name = 'uploadFile'),
    
    #Path for sending data to the oracle
    path('markov/<str:incomingStudents>/', views.testData.as_view(), name = 'testData'),

    #Path for creating a user
    url('createUser', views.createUser, name = 'createUser'),

    #Path for sending emails
    url('email', views.sendEmail, name = 'sendEmail'),

    #Path for giving permission
    path('permission/', views.givePerm, name = 'givePerm'),

]
