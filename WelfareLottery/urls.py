from django.conf.urls import url,include
from . import views

urlpatterns = [
  url(r'^info$', views.award_info),
  url(r'^get_type$', views.get_type)
]