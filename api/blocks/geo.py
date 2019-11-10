from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Track


def post_geo(data):
    try:
        track = Track.objects.filter(member_id=data['member']).update(coordinates=data['coordinates'])
    except:
        track = Track(member_id=data['member'], coordinates=data['coordinates'])
    try:
        track.save()
        return HttpResponse(renderers.JSONRenderer().render({'coordinates': track.coordinates}))
    except:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы КЭП!'}))