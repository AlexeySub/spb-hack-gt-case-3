from django.http import HttpResponse
from rest_framework import renderers


def get_data(data):
    return HttpResponse(renderers.JSONRenderer().render(data))
