from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Team, Token, Member


def create_team(data):
    boat = data['boat']
    for member in data['member']:
        team = Team(boat=boat, member=member)
        try:
            team.save()
            return HttpResponse(renderers.JSONRenderer().render({'status': '1'}))
        except db.DataError as e:
            return HttpResponse(renderers.JSONRenderer().render({
                'status': '0',
                'error': e
            }))


def get_team(data):
    teams = Team.objects.all().values()
    members = list()
    for team in teams:
        if team.boat == data['boat']:
            members.append(team.member)
    return HttpResponse(renderers.JSONRenderer().render(members))
