from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Team


def create_team(data):
    boat = data['boat']
    for member in data['member']:
        team = Team(boat=boat, member=member['member'])
        try:
            team.save()
            return HttpResponse(renderers.JSONRenderer().render({'status': '1'}))
        except db.DataError as e:
            return HttpResponse(renderers.JSONRenderer().render({
                'status': '0',
                'error': e
            }))
