from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('hubli/',views.hubli,name='hubli'),
    path('roles/',views.roles,name='roles'),


]