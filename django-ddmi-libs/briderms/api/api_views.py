from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import * 
from api.models import *

# class RulesPagination(LimitOffsetPagination):
#     default_limit = 10
#     max_limit = 100

class RuleList(ListAPIView):
  queryset = Rule.objects.all()
  serializer_class = RuleSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('rule_id', 'name', 'rule_store',)
  search_fields = ('description', 'statement', 'treatment_category')
  # pagination_class = RulesPagination

class RuleCreate(CreateAPIView):
  serializer_class = RuleSerializer

  def create(self, request, *args, **kwargs):
    try:
      name = request.data.get('name')
    except ValueError:
      raise ValidationError({ 'name': 'Null rule name is not allowed' })
    return super().create(request, *args, **kwargs)

class RulePacketList(ListAPIView):
  queryset = RulePacket.objects.all()
  serializer_class = RulePacketSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('rule_packet_id', 'name', 'rule_store',)
  search_fields = ('description', 'treatment_category', 'taggregation')

class RulePacketCreate(CreateAPIView):
  serializer_class = RulePacketSerializer

  def create(self, request, *args, **kwargs):
    try:
      name = request.data.get('name')
    except ValueError:
      raise ValidationError({ 'name': 'Null rule packet name is not allowed' })
    return super().create(request, *args, **kwargs)

class RulePackageList(ListAPIView):
  queryset = RulePackage.objects.all()
  serializer_class = RulePackageSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('rule_package_id', 'name', 'rule_store',)
  search_fields = ('description', 'taggregation')

class RuleStoreList(ListAPIView):
  queryset = RulePackage.objects.all()
  serializer_class = RuleStoreSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('rule_store_id', 'rule_store_name', 'realization',)
  search_fields = ('plan_acronym', 'plan', 'description', 'taggregation')

class DecisionTableList(ListAPIView):
  queryset = DecisionTable.objects.all()
  serializer_class = DecisionTableSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('decision_table_id', 'treatment_category_id', 'name')
  search_fields = ('description', 'taggregation')

class ScopeList(ListAPIView):
  queryset = Scope.objects.all()
  serializer_class = ScopeSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('scope_id', 'key', 'target_type')
  search_fields = ('description')

class TagList(ListAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('tag_id', 'key', 'tenant_key')
  search_fields = ('description')

class TaggregationList(ListAPIView):
  queryset = Taggregation.objects.all()
  serializer_class = TaggregationSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('taggregation_id', 'key', 'tenant_key')
  search_fields = ('description')

class TenantList(ListAPIView):
  queryset = Tenant.objects.all()
  serializer_class = TenantSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('tenant_id', 'name')
  search_fields = ('parent_tenant', 'description', 'acronym')

class TestCaseList(ListAPIView):
  queryset = TestCase.objects.all()
  serializer_class = TestCaseSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('test_case_id', 'rule_package', 'user_name')
  search_fields = ('test_case_data', 'change_date')

class TreatmentCategoryList(ListAPIView):
  queryset = TreatmentCategory.objects.all()
  serializer_class = TreatmentCategorySerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('treatment_category_id', 'name', 'precedence_order', 'realization_type', 'rule_store')
  search_fields = ('description', 'plan_acronym', 'taggregation')

class UserRoleList(ListAPIView):
  queryset = UserRole.objects.all()
  serializer_class = UserRoleSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('principal', 'role')
  search_fields = ()