from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from user.models import User
from score.models import Score
from django.views.decorators.csrf import csrf_exempt

class HomePageView(APIView):

    @csrf_exempt
    def create_or_retrieve(self, request=None, uname="test", format=None):
        if request.method == "GET":
            try:
                found_user = User.objects.get(name=uname)
                uid = found_user.id
                user_score = Score.objects.get(id=uid)
                data = { "user": uname, "score": user_score.score }
                return HttpResponse(json.dumps(data))
            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        if request.method == "POST":
            try:
                found_user = User.objects.get(name=uname)
                uid = found_user.id
                user_score = Score.objects.get(id=uid)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            s = Score(score=100)
            s.save()
            return HttpResponse(json.dumps({"status":"Success"}))

  
