from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Member, Role, Token
import secrets
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
        token = Token(user_id=member.id, token=secrets.token_hex(51))
        token.save()
        return HttpResponse(renderers.JSONRenderer().render({
            'id': member.id,
            'auth_token': token.token
        }))
    except Exception as e:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '0',
            'error': str(type(e))
        }))


def get_members():
    members = Member.objects.all().values()
    return HttpResponse(renderers.JSONRenderer().render(members.values()))


def login(data):
    try:
        member = Member.objects.get(email=data['email'])
        if member.password == func.Hash(data['password']):
            Token.objects.filter(user_id=member.id).update(token=secrets.token_hex(51))
            return HttpResponse(renderers.JSONRenderer().render({
                'auth_token': Token.objects.get(user_id=member.id).token,
                'member_id': member.id
            }))
    except Member.DoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '2',
            'error': 'DoesNotExist'
        }))


def get_role():
    roles = Role.objects.all()
    return HttpResponse(renderers.JSONRenderer().render(roles.values()))




