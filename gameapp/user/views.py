from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from user.models import User
from django.views.decorators.csrf import csrf_exempt

class HomePageView(APIView):

    @csrf_exempt
    def create_or_retrieve(self, request=None, uname="test", format=None):
        if request.method == "GET":
            try:
                found_user = User.objects.get(name=uname)
                data = { "user": uname, "id": found_user.id }
                return HttpResponse(json.dumps(data))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        if request.method == "POST":
            try:
                found_user = User.objects.get(name=uname)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = User(name=uname)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))
