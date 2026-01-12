from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Speler, Match_Punten


# Create your views here.
def start(request):
    return HttpResponse("welkom op de site van de PPL")


# een speler toevoegen
@csrf_exempt
def add_speler(request):
    post_data = json.loads(request.body.decode("utf-8"))
    nieuwe_speler = Speler()
    nieuwe_speler.naam = post_data["naam"]
    nieuwe_speler.voornaam = post_data["voornaam"]
    nieuwe_speler.email = post_data["email"]
    nieuwe_speler.save()

    return JsonResponse(model_to_dict(nieuwe_speler))

# een resultaat toevoegen
@csrf_exempt
def add_match_punten(request):
    post_data = json.loads(request.body.decode("utf-8"))
    nieuwe_match_gespeeld = Match_Punten()
    nieuwe_match_gespeeld.nummerSpeler = post_data["nummerSpeler"]
    nieuwe_match_gespeeld.punten = post_data["punten"]
    nieuwe_match_gespeeld.matchCode = post_data["matchCode"]
    nieuwe_match_gespeeld.save()

    return JsonResponse(model_to_dict(nieuwe_match_gespeeld))

# alle spelers weergeven
def alle_spelers(request):
    spelers = Speler.objects.all().values()

    return JsonResponse(list(spelers), safe=False)

# 1 speler weergeven op basis van id
def toon_speler(request, id):
    speler = Speler.objects.get(id = id)
    return JsonResponse(model_to_dict(speler))

