from django.urls import path,include
from . import views
urlpatterns = [
    path('<int:id>',views.index,name="index"),
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('trajets', views.trajets ,name="trajets"),
    path('reservations',views.reservations, name="reservations"),
    path('reservation/<int:id>',views.reservation, name="reservation"),
    path('nouvelle_reservation',views.edit_reservation,name="ajouter reservation"),
    path('edit_reservation/<int:id>',views.edit_reservation,name="modifier reservation"),
    path('infos',views.infos,name="informations")
    
]