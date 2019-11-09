from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Team, Token, Member


def create_team(data):
    print(data)
    token = Token.objects.get(token=data['auth_token'])
    for member in data['member']:
        team = Team(boat_id=Team.objects.get(member_id=token.user_id).boat_id, member_id=member)
        try: 
            Team.objects.filter(member_id=team.member_id)
            continue
        except:
            None
        try:
            team.save()
        except db.DataError as e:
            return HttpResponse(renderers.JSONRenderer().render({
                'status': '0',
                'error': e
            }))
    return HttpResponse(renderers.JSONRenderer().render("lol"))


def get_team(data):
    teams = Team.objects.all().values()
    members = list()
    for team in teams:
        if team.boat == data['boat']:
            members.append(team.member)
    return HttpResponse(renderers.JSONRenderer().render(members))
