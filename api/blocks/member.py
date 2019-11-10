from django.core import exceptions
from django.http import HttpResponse
from django import db
from rest_framework import renderers
from api.models import Member, Role, Token, Team
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
            'error': type(e)
        }))


def get_members(data):
    print(data)
    try:
        token = Token.objects.get(token=data['token'])
    except exceptions.ObjectDoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы неавторизованы!'}))
    if Member.objects.get(id=token.user_id).role_id == 1:
        members = Member.objects.filter(role_id=2)
        return HttpResponse(renderers.JSONRenderer().render(members.values()))
    else:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы КЭП!'}))
    
    
def get_member(data):
    
    memberr = Member.objects.get(id=data['id'])
    memberr.update({'role':Role.objects.get(id=memberr.role_id).name, 'boat':Boat.objects.get(id=Team.objects.get(user_id=memberr.id).boat_id).name})
    print(1)
    return HttpResponse(renderers.JSONRenderer().render(memberr.values()))

    return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы КЭП!'}))


    
def get_boat_members(data):
    try:
        token = Token.objects.get(token=data['token'])
    except exceptions.ObjectDoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы неавторизованы!'}))
    if Member.objects.filter(id=token.user_id).role_id == 1:
        members = Member.objects.get(id=Team.objects.get(boat_id=Team.objects.filter(member_id=token.user_id)).member_id)
        return HttpResponse(renderers.JSONRenderer().render(members.values()))
    else:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы КЭП!'}))
    

def login(data):
    try:
        member = Member.objects.get(email=data['email'])
        if member.password == func.Hash(data['password']):
            Token.objects.filter(user_id=member.id).update(token=secrets.token_hex(51))
            return HttpResponse(renderers.JSONRenderer().render({
                'auth_token': Token.objects.get(user_id=member.id).token,
                'member_id': member.id,
                'role': Role.objects.get(id=member.role_id).name
            }))
    except Member.DoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({
            'status': '2',
            'error': 'DoesNotExist'
        }))


def get_role():
    roles = Role.objects.all()
    return HttpResponse(renderers.JSONRenderer().render(roles.values()))




