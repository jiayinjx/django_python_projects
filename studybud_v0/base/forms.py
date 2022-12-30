from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
  class Meta:
    model = Room
    fields = '__all__' # create the form based on the model
    # field = ['name', 'body'] # add values you want to include
    