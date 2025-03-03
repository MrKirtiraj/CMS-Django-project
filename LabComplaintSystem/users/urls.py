from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('student/login/', views.student_login, name='student_login'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('complaints/', include('complaints.urls')),

]

#version-1 
"""
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('file_complaint/', views.dashboard, name='file_complaint'),
    path('complaints/', include('complaints.urls')),
    path('complaints/', include('complaints.urls')),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('', views.home, name='home'),  # Home page URL
]
"""

# kbtug22115 : kirtiRAJ123 : abc@xyz.com        Student
# teach1 : myteacheris1 : teach1@gmail.com      staff
# admin : myadminis1 : admin@gmail.com          admin