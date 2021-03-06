from django import views
from rest_framework import parsers, renderers
from api.blocks import boat, member, team, mobile, geo, event


class Member(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return member.register_member(data)

    def get(self, request):
        print(request)
        return member.get_members(request.GET)
        data = parsers.JSONParser().parse(request)
        
        
class MemberLogin(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        print(request)
        return member.login(data)
    
    def get(self, request):
        return member.get_boat_members(request.GET)

    
class Geo(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        return geo.post_geo(data)
    
    def get(self, request):
        return geo.get_geo(request.GET)
    

class Role(views.View):
    def get(self, request):
        return member.get_role()
    
    
class Profile(views.View):
    def get(self, request):
        return member.get_member(request.GET)


class Class(views.View):
    def get(self, request):
        return boat.get_boat_class()
    
    
class Events(views.View):
    def get(self, request):
        return event.get_events()

    
class Event(views.View):
    def get(self, request):
        return event.get_event(request.GET)
    

class Boat(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return boat.register_boat(data)

    def get(self, request):
        return boat.get_boat()


class Team(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return team.create_team(data)

    def get(self, request):
        return team.get_team(parsers.JSONParser().parse(request))


class Mobile(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return mobile.get_data(data)

    def get(self, request):
        print(request.GET)
        return mobile.get_data(request.GET)
