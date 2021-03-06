from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Track


def post_geo(data):
    try:
        track = Track.objects.get(member_id=data['member'])
        Track.objects.filter(member_id=data['member']).update(coordinates=data['coordinates'])
        return HttpResponse(renderers.JSONRenderer().render({'coordinates': data['coordinates']}))
    except Track.DoesNotExist:
        track = Track(member_id=data['member'], coordinates=data['coordinates'])
        track.save()
        return HttpResponse(renderers.JSONRenderer().render({'coordinates': track.coordinates}))
    
    
def get_geo(data):
    
    track = Track.objects.get(member_id=data['member'])
    return HttpResponse(renderers.JSONRenderer().render({'coordinates': track.coordinates}))

