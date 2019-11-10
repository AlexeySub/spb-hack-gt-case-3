from django.http import HttpResponse
from rest_framework import renderers
from api.models import Events


def get_events():
    events = Events.objects.all().values()
    return HttpResponse(renderers.JSONRenderer().render(events.values()))


def get_event(data):
    try:
        event = Events.objects.get(id=data['id'])
        return HttpResponse(renderers.JSONRenderer().render({'name':event.name, 'desc':event.description, 
                                                             'date':event.date}))
    except:
        return HttpResponse(renderers.JSONRenderer().render({'error':'KEP'}))
