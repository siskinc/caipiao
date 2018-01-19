from rest_framework import serializers
from HighFrequencyLottery.models import MetaHighFrequencyLottery
class HighFrequencyLotterySerializer(serializers.ModelSerializer):
  class Meta:
    model = MetaHighFrequencyLottery
    fields = ('trem', 'data_award', 'value3', 'value4', 'value5')