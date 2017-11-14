from django.conf.urls import include,url
from . import webhook

urlpatterns = [
    url(r'^v1/webhook$', webhook.set_location, name='webhook_set_location'),
]
