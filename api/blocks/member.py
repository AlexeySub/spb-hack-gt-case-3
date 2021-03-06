from django.core import exceptions
from django.http import HttpResponse
from django import db
from rest_framework import renderers, parsers
from api.models import Member, Role, Token, Team, Boat, BoatClass
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
                    password=func.Hash(data['password']),
                    take_part_flag=data['take_part_flag'])
    
    try:
        member.save()
        token = Token(user_id=member.id, token=secrets.token_hex(51))
        token.save()
        return HttpResponse(renderers.JSONRenderer().render({
            'member_id': member.id,
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
        members = Member.objects.filter(role_id=2, take_part_flag=True)
        return HttpResponse(renderers.JSONRenderer().render(members.values()))
    else:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы КЭП!'}))
    
    
def get_member(data):
    member = Member.objects.get(id=data['id'])
    try:
        boat_name = Boat.objects.get(id=Team.objects.get(member_id=member.id).boat_id).name
        boat_number = Boat.objects.get(id=Team.objects.get(member_id=member.id).boat_id).boat_number
        boat_tech = Boat.objects.get(id=Team.objects.get(member_id=member.id).boat_id).tech_inspection
        boat_class = BoatClass.objects.get(id=Boat.objects.get(id=Team.objects.get(member_id=member.id)).boat_class_id).name
    except:
        boat_name = "none"
        boat_number = "none"
        boat_tech = "none"
        boat_class = "none"
    return HttpResponse(renderers.JSONRenderer().render({
        'first_name':member.first_name,
        'last_name':member.last_name,
        'patronymic':member.patronymic,
        'phone_number':member.phone_number,
        'role':Role.objects.get(id=member.role_id).name,
        'email':member.email,
        'passport':member.passport,
        'boat_name':boat_name,
        'boat_number': boat_number,
        'boat_tech': boat_tech,
        'boat_class': boat_class,
    }))

    
def get_boat_members(data):
    try:
        token = Token.objects.get(token=data['token'])
    except exceptions.ObjectDoesNotExist:
        return HttpResponse(renderers.JSONRenderer().render({'error': 'Вы неавторизованы!'}))
    if Member.objects.get(id=token.user_id).role_id == 1:
        team = Team.objects.filter(boat_id=Team.objects.get(member_id=token.user_id).boat_id)
        list = []
        for i in team:
            list.append(i.member_id)
        members = Member.objects.filter(id__in=list)
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




