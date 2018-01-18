from django.db import models

class HighFrequencyLottery(models.Model):
  name = models.CharField('种类名称', max_length=20, null=False)
  trem = models.CharField('期数', max_length=20, null=False)

class MetaHighFrequencyLottery(models.Model):
  trem = models.CharField('期数', max_length=20, null=False)
  data_award = models.CharField('开奖号码', max_length=20, null=False)
  value3 = models.CharField('value3', max_length=20, null=False)
  value4 = models.CharField('value4', max_length=20, null=False)
  value5 = models.CharField('value5', max_length=20, null=True)
  type_trem = models.ForeignKey(HighFrequencyLottery, null=False, on_delete=models.CASCADE)