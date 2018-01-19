from datetime import datetime
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from HighFrequencyLottery.models import HighFrequencyLottery,MetaHighFrequencyLottery
from HighFrequencyLottery.serializers import HighFrequencyLotterySerializer

class MetaHighFrequencyLotteryList(APIView):

  def get_object(self, type_trem_id):
    try:
      meta_high_frequency_lottery_list = MetaHighFrequencyLottery.objects.filter(type_trem_id = type_trem_id)
    except MetaHighFrequencyLottery.DoesNotExist:
      raise Http404
    return meta_high_frequency_lottery_list

  def get_type_trem_id(self, name, today_trem):
    try:
      types = HighFrequencyLottery.objects.filter(name=name, trem=today_trem)
    except HighFrequencyLottery.DoesNotExist:
      raise Http404
    if len(types) == 0:
      raise Http404
    type_trem_id = types[0].pk
    return type_trem_id

  def get(self, request, name):
    today_trem = datetime.now().strftime('%Y%m%d')
    type_trem_id = self.get_type_trem_id(name, today_trem)
    meta_high_frequency_lottery_list = self.get_object(type_trem_id)
    serializer = HighFrequencyLotterySerializer(meta_high_frequency_lottery_list, many=True)
    return Response(serializer.data)
