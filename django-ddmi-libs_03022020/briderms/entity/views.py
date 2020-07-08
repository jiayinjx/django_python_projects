from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory


from api.models import Rule, RulePacket, RulePackage, RuleStore, DecisionTable
from .forms import *

def entityHome(request):
  rules = Rule.objects.all()
  rulepackets = RulePacket.objects.all()
  rulepackages = RulePackage.objects.all()
  rulestores = RuleStore.objects.all()
  decisiontables = DecisionTable.objects.all()

  total_rules = rules.count()
  total_rulepackets = rulepackets.count()
  total_rulepackages = rulepackages.count()
  total_rulestores = rulestores.count()
  total_decisiontables = decisiontables.count()

  context = {'rules':rules, 'rulepackets':rulepackets, 'rulepackages':rulepackages, 'rulestores':rulestores, 'decisiontables':decisiontables, 'total_rules':total_rules, 'total_rulepackets':total_rulepackets, 'total_rulepackages': total_rulepackages, 'total_rulestores': total_rulestores, 'total_decisiontables': total_decisiontables}

  return render(request, 'entity/dashboard.html', context)

def rules(request):
  # rules = Rule.objects.all()
  rules = Rule.objects.order_by('start_date')[:30]
  return render(request, 'entity/ruleList.html', {'rules': rules})

def rulepackets(request):
  rulepackets = RulePacket.objects.all()[:100]
  return render(request, 'entity/rulepacketList.html', {'rulepackets': rulepackets})

def rulestores(request):
  rulestores = RuleStore.objects.all()[:100]
  return render(request, 'entity/rulestoreList.html', {'rulestores': rulestores})