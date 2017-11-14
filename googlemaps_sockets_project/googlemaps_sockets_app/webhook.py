import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models
from channels import Group

@csrf_exempt
def set_location(request):
    data = json.loads(request.body)
    print(data)
    zipcode = models.ZipCodePlace(
        zipcode = data["zipcode"],
        lat = data["lat"],
        lng = data["lng"]
    )
    print(data)
    Group('maps').send(
        {"text": json.dumps(data)}
    )
    # Send to connected users
    return HttpResponse('ok')
