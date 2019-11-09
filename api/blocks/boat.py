from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Boat


def register_boat(data):
    boat = Boat(name=data['name'], class_id=data['class'], boat_number=data['boat_number'],
                tech_inspection=data['tech_inspection'], max_members=data['max_members'])

    try:
        boat.save()
        return HttpResponse(renderers.JSONRenderer().render({'status': '1'}))
    except db.IntegrityError:
        return HttpResponse(renderers.JSONRenderer().render({'status': '0'}))


def get_boat(data):
    boat = Boat.objects.filter(id=data['id'])
    return HttpResponse(renderers.JSONRenderer().render(boat.values()))