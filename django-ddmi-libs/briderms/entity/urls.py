from django.urls import path
# from django.http import HttpResponse
from . import views

urlpatterns = [
  path('', views.entityHome, name="entityhome"),
  path('rules/', views.rules, name="entity_rules"),
  path('rulepackets/', views.rulepackets, name="entity_rulepackets"),
  path('rulestores/', views.rulestores, name="entity_rulestores"),
  # path('rule/<str:rule_pk>', views.rule, name="entity_rule"),
]