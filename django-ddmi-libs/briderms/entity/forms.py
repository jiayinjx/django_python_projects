from django.forms import ModelForm
from django import forms


from api.models import Rule, RulePacket, RulePackage, RuleStore, DecisionTable


class RuleForm(ModelForm):
  class Meta:
    model = Rule
    fields = '__all__'

class RulePacketForm(ModelForm):
  class Meta:
    model = RulePacket
    fields = '__all__'

class RulePacketForm(ModelForm):
  class Meta:
    model = RulePacket
    fields = '__all__'

class RulePackageForm(ModelForm):
  class Meta:
    model = RulePackage
    fields = '__all__'

class RuleStoreForm(ModelForm):
  class Meta:
    model = RuleStore
    fields = '__all__'

class DecisionTableForm(ModelForm):
  class Meta:
    model = DecisionTable
    fields = '__all__'