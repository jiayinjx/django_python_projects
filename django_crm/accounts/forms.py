from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
        # fields = ['customer', 'product']
