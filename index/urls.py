from django.urls import path
from . import views
app_name='indexurl'
urlpatterns = [
    
	path('', views.myindex, name='index'),
	path('about/<slug>/', views.myabout, name='about'),
	path('list/', views.myservices, name='celeb'),
	path('contact/', views.mycontact, name='contact'),
	path('track/', views.mytrack, name='track'),
	path('quote/', views.myquote, name='quote'),
	path('dash/', views.dash, name='dash'),
	path('search/', views.search, name='search'),
	path('tickets-lists/', views.tic, name="tic"),
    path('my-card/', views.mycard, name='card'),

]