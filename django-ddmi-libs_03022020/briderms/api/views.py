from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from api.serializers import UserSerializer, GroupSerializer
from api.serializers import *
from api.models import *

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

def permission_denied_handler(request):
  from django.http import HttpResponse
  return HttpResponse('you have no permissions!')

@csrf_exempt
def authgroup_list(request):
  """
  List all authgroups, or create a new authgroup.
  """
  if request.method == 'GET':
    authgroups = AuthGroup.objects.all()
    serializer = AuthGroupSerializer(authgroups, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = AuthGroupSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def authgroup_detail(request, pk):
  """
  Retrieve, update or delete a authgroup.
  """
  try:
    authgroup = AuthGroup.objects.get(pk=pk)
  except authgroup.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = AuthGroupSerializer(authgroup)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = AuthGroupSerializer(authgroup, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    authgroup.delete()
    return HttpResponse(status=204)

@csrf_exempt
def decisiontable_list(request):
  if request.method == 'GET':
    decisiontables = DecisionTable.objects.all()
    serializer = DecisionTableSerializer(decisiontables, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = DecisionTableSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def decisiontable_detail(request, pk):
  try:
    decisiontable = DecisionTable.objects.get(pk=pk)
  except authgroup.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = DecisionTableSerializer(decisiontable)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = DecisionTableSerializer(decisiontable, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    authgroup.delete()
    return HttpResponse(status=204)









































@csrf_exempt
def carrier_list(request):
  """
  List all carriers, or create a new carrier.
  """
  if request.method == 'GET':
    carriers = Carrier.objects.all()
    serializer = CarrierSerializer(carriers, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = CarrierSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def carrier_detail(request, pk):
  """
  Retrieve, update or delete a carrier.
  """
  try:
    carrier = Carrier.objects.get(pk=pk)
  except carrier.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = CarrierSerializer(carrier)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = CarrierSerializer(carrier, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    carrier.delete()
    return HttpResponse(status=204)

@csrf_exempt
def rule_list(request):
  """
  List all rules, or create a new rule.
  """
  if request.method == 'GET':
    rules = Rule.objects.all()
    serializer = RuleSerializer(rules, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = RuleSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def rule_detail(request, pk):
  """
  Retrieve, update or delete a rule.
  """
  try:
    rule = Rule.objects.get(pk=pk)
  except rule.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = RuleSerializer(rule)
    return JsonResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = RuleSerializer(rule, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    rule.delete()
    return HttpResponse(status=204)