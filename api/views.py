from django import views
from rest_framework import parsers, renderers
from api.blocks import boat, member


class Member(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return member.register_member(data)
    def get(self, request):
        return member.get_members()


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
