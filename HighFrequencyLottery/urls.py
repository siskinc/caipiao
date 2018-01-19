from django.conf.urls import url,include
from . import views

urlpatterns = [
  url(r'^(?P<name>.+)$', views.MetaHighFrequencyLotteryList.as_view())
]
