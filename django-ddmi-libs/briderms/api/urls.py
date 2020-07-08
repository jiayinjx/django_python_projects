from django.urls import path
from api import views, api_views

urlpatterns = [
  path('rules', api_views.RuleList.as_view()),
  path('rules/new', api_views.RuleCreate.as_view()),
  path('rule-packets', api_views.RulePacketList.as_view()),
  path('rule-packages', api_views.RulePackageList.as_view()),
  path('rule-stores', api_views.RuleStoreList.as_view()),
  path('decision-tables', api_views.DecisionTableList.as_view()),
  path('scopes', api_views.ScopeList.as_view()),
  path('tags', api_views.TagList.as_view()),
  path('taggregations', api_views.TaggregationList.as_view()),
  path('tenants', api_views.TenantList.as_view()),
  path('test-cases', api_views.TestCaseList.as_view()),
  path('treatment-categorys', api_views.TreatmentCategoryList.as_view()),
  path('user-roles', api_views.UserRoleList.as_view()),
  path(r'views/carriers', views.carrier_list),
  path(r'views/carriers/<int:pk>/', views.carrier_detail),
  path(r'views/rules', views.rule_list),
  path(r'views/rules/<int:pk>/', views.rule_detail),
  path(r'views/autogroups', views.authgroup_list),
  path(r'views/autogroups/<int:pk>/', views.authgroup_detail),
  path(r'views/decisiontables', views.decisiontable_list),
  path(r'views/decisiontables/<int:pk>/', views.decisiontable_detail),
]