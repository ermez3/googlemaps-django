import json
from channels.auth import channel_session_user_from_http,channel_session_user
from .models import ZipCodePlace
from channels import Group

def ws_connect(message):
    Group('maps').add(message.reply_channel)
    message.reply_channel.send({"accept" : True})
    print('Conectado')

def ws_disconnect(message):
    Group('maps').discard(message.reply_channel)

def ws_receive(message):
    pass
