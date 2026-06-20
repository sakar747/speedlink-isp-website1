from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('support/', views.support, name='support'),
    path('assistant/', views.assistant, name='assistant'),
    path('assistant/reply/', views.assistant_reply, name='assistant_reply'),
    path('submit-complaint/', views.submit_complaint, name='submit_complaint'),
    path('complaint-success/<str:reference_number>/', views.complaint_success, name='complaint_success'),
    path('track-complaint/', views.track_complaint, name='track_complaint'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('staff/logout/', views.staff_logout, name='staff_logout'),
    path('staff/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff/complaint/<str:reference_number>/', views.complaint_detail, name='complaint_detail'),
    path('staff/complaint/<str:reference_number>/update/', views.update_complaint, name='update_complaint'),
]
