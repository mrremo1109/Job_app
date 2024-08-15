<<<<<<< HEAD
from django.shortcuts import redirect
=======
>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registerRecruiter/', views.registerRecruiter, name='registerRecruiter'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('profile/', views.profile, name='profile'),
    path('logoutUser/', views.logoutuser, name='logoutUser'),
    path('apply/<str:job_id>', views.apply, name='apply'),
    path('addPost/' , views.addPost, name='addPost'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
    path('search/', views.searched, name='search'),
    path('manage_applications/', views.manage_applications, name='manage_applications'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('application/<int:application_id>/update/', views.update_application_status, name='update_application_status'),
    path('accept_application/<int:application_id>/', views.accept_application, name='accept_application'),
<<<<<<< HEAD
    path('reject_application/<int:application_id>/', views.reject_application, name='reject_application'), 
    path('chat/<int:receiver_id>/messages/', views.retrieve_chat_messages, name='retrieve_chat_messages'),
    path('chat/send/', views.send_message, name='send_message'),
=======
    path('reject_application/<int:application_id>/', views.reject_application, name='reject_application'),   
>>>>>>> cea0c8b141975ab6ace93ba729c91aad997cb299
]