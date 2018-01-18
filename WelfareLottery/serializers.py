from rest_framework import serializers
from WelfareLottery.models import WelfareLottery

class WelfareLotterySerializer(serializers.ModelSerializer):
  class Meta:
    model = WelfareLottery
    fields = ('name', 'trem', 'time', 'sale', 'pool', 'matchboll', 'bonus',)