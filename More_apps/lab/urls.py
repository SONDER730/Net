from django.contrib import admin
from django.urls import path,include
from More_apps.lab import views


urlpatterns=[
    path('',views.lab,name='lab'),
    path('class1',views.class1,name='class1'),
    path('class2',views.class2,name='class2'),
    path('class3',views.class3,name='class3'),
    path('class4',views.class4,name='class4'),
]