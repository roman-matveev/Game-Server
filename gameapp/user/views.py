from django.http import HttpResponse
from rest_framework.views import APIView
import json

# Create your views here.
class HomePageView(APIView):
    def get(self, request=None, uname="test", format=None):
        try:
            found_user = User.objects.get(name=uname)
        except ObjectDoesNotExist as e:
            return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        data = { "user": uname, "id": found_user.id }
        return HttpResponse(json.dumps(data))
