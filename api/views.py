from django import views
from rest_framework import parsers, renderers
from api.blocks import boat, member, team, mobile


class Member(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return member.register_member(data)

    def get(self, request):
        return member.get_members(request.GET)


class MemberLogin(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        print(request)
        return member.login(data)


class Role(views.View):
    def get(self, request):
        return member.get_role()


class Class(views.View):
    def get(self, request):
        return boat.get_boat_class()


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