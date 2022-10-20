from django.urls import path

from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('alldp',views.alldp,name='alldp'), 
     path('dashboard',views.dashboard,name='dashboard'), 
     path('create',views.create,name='create'), 
     path('avatar',views.avatar,name='avatar'),
     path('preview',views.preview,name='preview'),
     path('publish',views.publish,name='publish'), 
     path('visitor1/<int:pk>',views.visitor1,name='visitor1'),
     path('visitor2/<int:pk>',views.visitor2,name='visitor2'),
     path('category',views.category,name='category'),
     path('category/<str:cat>',views.categories,name='categories'),
     #path('',views.,name=''),  
]