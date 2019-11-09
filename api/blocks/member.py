from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Member


def register_member(data):
    try:
        member = Member.objects.get(email=data['email'])
        return HttpResponse(renderers.JSONRenderer().render({'status': '2'}))
    except:
        None
    member = Member(first_name=data['first_name'], last_name=data['last_name'], email=data['email'],
                 patronymic=data['patronymic'], phone_number=data['phone_number'], role_id=data['role'],
                 swimming_skill=data['swimming_skill'], password=data['password'])
    #if data['passport'] != '':
    try:
        member.save()
        return HttpResponse(renderers.JSONRenderer().render({'id': member.id}))
    except db.IntegrityError:
        return HttpResponse(renderers.JSONRenderer().render({'status': '0'}))


def login(data):
    try:
        member = Member.objects.filter(email=data['email'])
    except:
        return HttpResponse(renderers.JSONRenderer().render({'status': '2'}))
    if member.password == data['password']:
        return HttpResponse(renderers.JSONRenderer().render(member.values()))
    else:
        return HttpResponse(renderers.JSONRenderer().render({'status': '3'}))



