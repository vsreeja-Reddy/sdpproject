from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/',views.projecthomepage,name='projecthomepage'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('',views. login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login1/', views.login1, name='login1'),
    path('signup1/', views.signup1, name='signup1'),
    path('logout/', views.logout, name='logout'),
    path('donate/',views.donate,name='donate'),
    path('urgent/',views.urgent,name='urgent'),
    path('animals/',views.animals,name='animals'),
    path('children/',views.children,name='children'),
    path('hungry/',views.hungry,name='hungry'),
    path('disability/',views.disability,name='disability'),
    path('medical/',views.medical,name='medical'),
    path('education/',views.education,name='education'),
    path('women/',views.women,name='women'),
    path('feedback/',views.feedback_view, name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('donate_now/', views.donate_now, name='donate_now'),
    path('donate/process/', views.process_donation, name='process_donation'),
    path('children_donate/', views.children_donate, name='children_donate'),
    path('submit_details/', views.submit_details, name='submit_details'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('animal_donate/', views.animal_donate, name='animal_donate'),
    path('donation_cards/',views.donation_cards,name='donation_cards'),
    path('contact1/', views.contact1, name='contact1'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


