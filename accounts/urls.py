from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.trying2, name='login'),
    path('logout', views.logout, name='logout'),
]
