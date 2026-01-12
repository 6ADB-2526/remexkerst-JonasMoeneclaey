from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('speler/', views.alle_spelers),
    path('speler/add', views.add_speler),
    path('speler/<int:id>', views.toon_speler),
    path('matchgespeeld/add', views.add_match_punten),
    path('matchPunten/resultaat/<int:idSpeler>/<int:matchCode>', views.uitslag_speler),
    path('punten/<int:idSpeler>', views.tot_punten_speler),
    
]