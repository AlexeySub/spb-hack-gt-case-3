from django.urls import path
from api import views


urlpatterns = [
    path('member/', views.Member.as_view()),
    path('member/login/', views.MemberLogin.as_view()),
    path('boat/', views.Boat.as_view()),
    path('role/', views.Role.as_view()),
    path('class/', views.Class.as_view()),
    path('team/', views.Team.as_view()),
    path('mobile/', views.Mobile.as_view()),
    path('profile/', views.Profile.as_view()),
    path('geo/', views.Geo.as_view()),
]
