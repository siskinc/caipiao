from django.db import models


class WelfareLottery(models.Model):
  name = models.CharField('彩票名字', max_length=20 ,null=False)
  trem = models.CharField('期', max_length=20, null=False)
  time = models.CharField('开奖时间', max_length=30, null=False)
  sale = models.CharField('全国销量', max_length=30, null=False)
  pool = models.CharField('奖池奖金', max_length=30, null=False)
  matchboll = models.CharField('开奖号码', max_length=50, null=False)
  bonus = models.CharField('开奖信息', max_length=300, null=False)

  class Meta:
    ordering = ('name',)

