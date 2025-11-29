from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about.html', views.about, name='about_html'),
    path('blog/', views.blog, name='blog'),
    path('blog.html', views.blog, name='blog_html'),
    path('contact/', views.contact, name='contact'),
    path('contact.html', views.contact, name='contact_html'),
    path('event/', views.event, name='event'),
    path('event.html', views.event, name='event_html'),
    path('program/', views.program, name='program'),
    path('program.html', views.program, name='program_html'),
    path('service/', views.service, name='service'),
    path('service.html', views.service, name='service_html'),
    path('team/', views.team, name='team'),
    path('team.html', views.team, name='team_html'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('testimonial.html', views.testimonial, name='testimonial_html'),
]