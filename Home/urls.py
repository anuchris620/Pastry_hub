
from django.urls import path
from . import views 
urlpatterns = [
    
    path( 'test/',views.ind),
    path('',views.index),
    path('login/',views.log, name='loginpage'),
    path('register/',views.reg, name='regipage'),
    path('logout/',views.logt)
]