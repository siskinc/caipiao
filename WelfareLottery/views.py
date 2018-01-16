from django.shortcuts import render
from django.http import JsonResponse,Http404,HttpResponse
from django.db import models
from django.forms.models import model_to_dict
from simplejson import dumps
from . import models

def award_info(request):
  if request.method == 'GET':
    raise Http404('Page not found')
  name = request.POST.get('name','')
  num = request.POST.get('num','')
  if name in (None, '') or num in (None, ''):
    return JsonResponse('text', 'name or num are need')
  if not num.isdigit():
    return JsonResponse('text', 'num must be a digit')
  if int(num) > 30:
    return JsonResponse('text', 'num must less than 30')
  infos = models.WelfareLottery.objects.filter(name=name)[:int(num)]
  result = []
  print(type(model_to_dict(infos[0])))
  for info in infos:
    result.append(model_to_dict(info))
  return HttpResponse(str(result).encode('utf-8'), content_type='application/json')


def get_type(request):
  if request.method == 'POST':
    return JsonResponse('text', 'not found')
  names = models.WelfareLottery.objects.values('name').distinct()
  result = ''
  count = 0
  names = list(names)

  for name in names:
    if count == 0:
      result = result + name['name']
    else:
      result = result + '|' + name['name']
    count = count + 1
  return HttpResponse(dumps({'types':result}), content_type='application/json')