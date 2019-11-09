from django.urls import path
from api import views


urlpatterns = [
    path('member/', views.Member.as_view()),
    path('member/login/', views.MemberLogin.as_view()),
    path('boat/', views.Boat.as_view()),
    path('role/', views.Role.as_view()),
    path('class/', views.Class.as_view()),
]
