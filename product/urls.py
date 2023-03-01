from django.urls import path
from . import views 


urlpatterns = [
    
    #path('',views.prodetails,name='details'),
    #path('',views.prodetails2,name='details'),
    path('',views.prodetails,name='details'),
    path('cmd/',views.commentarea, name='cmtpage')
]