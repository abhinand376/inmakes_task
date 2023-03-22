from . import views
from django.urls import path


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('newpage',views.btnhome,name='btnhome'),
    path('form',views.formpage,name='formpage'),
    path('logout',views.logout,name='logout'),
    path('successpage',views.successpage,name='successpage'),
    path('cs',views.cs,name='cs')

    ]