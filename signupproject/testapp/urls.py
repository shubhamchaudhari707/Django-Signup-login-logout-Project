
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signups, name='signup'),
    path('login/',views.logins, name='login'),
    path('logout/',views.logouts, name='logout'),
]