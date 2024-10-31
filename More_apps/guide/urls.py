from django.contrib import admin
from django.urls import path,include
from More_apps.guide import views


urlpatterns=[
    path('',views.guide,name='guide'),
    path('question1',views.question1,name='question1'),
    path('question2',views.question2,name='question2'),
    path('question3',views.question3,name='question3'),
    path('question4',views.question4,name='question4'),
    path('consult',views.consult,name='consult'),
    path('feedback',views.feedback,name='feedback'),
]