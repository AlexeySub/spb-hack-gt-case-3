from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

application = ProtocolTypeRouter({
    'websocket': URLRouter(api.routing.websocket_urlpatterns)
})