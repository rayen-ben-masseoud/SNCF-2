from django.urls import path,include
from . import views
urlpatterns = [
    path('<int:id>',views.index,name="index"),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('trajets', views.trajets ,name="trajets"),
    path('reservations',views.reservations, name="reservations"),
    path('reservation/<int:id>',views.reservation, name="reservation"),
    
    
    
]