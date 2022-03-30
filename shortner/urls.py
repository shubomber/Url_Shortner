from django.urls import path
from . import views

#urlconfiguration
urlpatterns = [
    path('',views.homescreen, name='homescreen'),
    path('create',views.create,name='create'),
    path('<str:pk>',views.go,name='go')
]