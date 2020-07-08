from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class AuthGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthGroup
    fields = '__all__'

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthGroupPermissions
    fields = '__all__'

class AuthPermissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthPermission
    fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthUser
    fields = '__all__'

class AuthUserGroupsSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthUserGroups
    fields = '__all__'

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = AuthUserUserPermissions
    fields = '__all__'

class BrideUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = BrideUser
    fields = '__all__'

class CarrierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carrier
    fields = '__all__'
    # fields = ['carrier_id', 'accronym', 'name', 'user_name', 'appl']

class ChangeRequestSerializer(serializers.ModelSerializer):
  class Meta:
    model = ChangeRequest
    fields = '__all__'

class ClaimsDeplRulePkgAuditSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClaimsDeplRulePkgAudit
    fields = '__all__'

class ClaimsDeployedRulePkgSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClaimsDeployedRulePkg
    fields = '__all__'

class CountySerializer(serializers.ModelSerializer):
  class Meta:
    model = County
    fields = '__all__'

class DecisionTableSerializer(serializers.ModelSerializer):
  class Meta:
    model = DecisionTable
    fields = '__all__'

class DecisionTableAuditSerializer(serializers.ModelSerializer):
  class Meta:
    model = DecisionTableAudit
    fields = '__all__'

class DecisionTableSnapshotSerializer(serializers.ModelSerializer):
  class Meta:
    model = DecisionTableSnapshot
    fields = '__all__'






class RuleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rule
    fields = '__all__'

class RulePacketSerializer(serializers.ModelSerializer):
  class Meta:
    model = RulePacket
    fields = '__all__'

class RulePackageSerializer(serializers.ModelSerializer):
  class Meta:
    model = RulePackage
    fields = '__all__'

class RuleStoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = RuleStore
    fields = '__all__'

class DecisionTableSerializer(serializers.ModelSerializer):
  class Meta:
    model = DecisionTable
    fields = '__all__'

class ScopeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Scope
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'

class TaggregationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Taggregation
    fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tenant
    fields = '__all__'

class TestCaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = TestCase
    fields = '__all__'

class TreatmentCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = TreatmentCategory
    fields = '__all__'

class UserRoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserRole
    fields = '__all__'
