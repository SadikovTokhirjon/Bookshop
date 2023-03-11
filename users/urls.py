from django.urls import path
from users.views import Registertion,LoginView,ProfileView,LogoutView,UserUpadeView
app_name='users'
urlpatterns=[
    path('singup/',Registertion.as_view(),name='singup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('profile/edit',UserUpadeView.as_view(),name='profile-edit'),

]