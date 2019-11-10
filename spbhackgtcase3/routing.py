from channels.routing import route
from api.consumers import ws_message, ws_add

channel_routing = [
    route("websocket.connect", ws_add, path=r'^/mobile/$'),
    route("websocket.receive", ws_message, path=r'^/mobile/$', method=r"^GET$"),
]
