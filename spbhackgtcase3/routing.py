from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing
from django.conf.urls import url
from api import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url("ws://spb-hack-gt-case-3.herokuapp.com/mobile/", consumers.Consumer)
    ])
})