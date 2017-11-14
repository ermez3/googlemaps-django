from channels import include

channel_routing = [
    include("googlemaps_sockets_app.routing.channel_routing", path=r'^/webhook/map/'),
]
