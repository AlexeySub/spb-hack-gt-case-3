from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Member, Role
from api.common import func


def register_member(data):
    member = Member(first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    patronymic=data['patronymic'],
                    phone_number=data['phone_number'],
                    role_id=data['role'],
                    swimming_skill=data['swimming_skill'],
                    password=func.Hash(data['password']))
    
    try:
        member.save()
        return HttpResponse(renderers.JSONRenderer().render({'id': member.id}))
    except Exception as e:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '0',
            'error': type(e)
        }))


def get_members():
    members = Member.objects.all().values()
    return HttpResponse(renderers.JSONRenderer().render(members.values()))


def login(data):
    try:
        memberr = Member.objects.get(email=data['email'])
        if memberr.password == func.Hash(data['password']):
            return HttpResponse(renderers.JSONRenderer().render(memberr.values()))
    except Member.DoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '2',
            'error': 'DoesNotExist'
        }))
"""
    try:
        member = Member.objects.filter(email=data['email'])
        member = Member.objects.get(email=data['email'])
    except Exception as e:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '2',
            'error': type(e)
        }))
    print(data)
    print(data['password'])
    if member.password == func.Hash(data['password']):
        data.session[data['email']] = member.email
        return HttpResponse(renderers.JSONRenderer().render(member.values()))
    else:
        return HttpResponse(renderers.JSONRenderer().render({'status': '3'}))
"""


def get_role():
    roles = Role.objects.all()
    return HttpResponse(renderers.JSONRenderer().render(roles.values()))




