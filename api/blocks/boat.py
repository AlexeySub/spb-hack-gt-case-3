from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Boat, Team, BoatClass


def register_boat(data):
    boat = Boat(name=data['name'], class_id=data['boat_class'], boat_number=data['boat_number'],
                tech_inspection=data['tech_inspection'])

    team = Team(boat_id=boat.id, member_id=data['member'])

    try:
        boat.save()
        team.save()
        return HttpResponse(renderers.JSONRenderer().render({'status': '1'}))
    except db.DataError as e:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '0',
            'error': e
        }))


def get_boat(data):
    boat = Boat.objects.filter(id=data['id'])
    return HttpResponse(renderers.JSONRenderer().render(boat.values()))


def get_boat_class():
    classes = BoatClass.objects.all()
    return HttpResponse(renderers.JSONRenderer().render(classes.values()))
