
from django.urls import path
from . import views 
from .field import cakeupdate 
urlpatterns = [
    
    path( 'test/',views.ind),
    path('',views.index, name='home'),
    path('login/',views.log, name='loginpage'),
    path('register/',views.reg, name='regipage'),
    path('logout/',views.logt),
    path('srh/',views.search, name='search'),
    path('autocom/',views.autocom, name='auto'),
    path('feed/',cakeupdate()),                                  #  path('feed/',field.cakeupdate()
     
]
