from django.urls import path 
from . import views 

urlpatterns = [
    path('sign_up/',views.sign_up,name='user-sign_up'),
    path('profile/',views.profile,name='user-profile'),
    path('profile/update/',views.profile_update,name='user-profile-update'),
   
]