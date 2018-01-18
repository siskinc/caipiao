from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from WelfareLottery.models import WelfareLottery
from WelfareLottery.serializers import WelfareLotterySerializer

class WelfareLotteryList(APIView):

  def get_object(self, name):
    try:
      welfare_lottery_list = WelfareLottery.objects.filter(name=name)
    except WelfareLottery.DoesNotExist:
      raise Http404
    return welfare_lottery_list

  def get(self, request, name):
    num = int(request.GET.get('num','10'))
    welfare_lottery_list = self.get_object(name=name)[:num]
    serializer = WelfareLotterySerializer(welfare_lottery_list, many=True)
    return Response(serializer.data)
