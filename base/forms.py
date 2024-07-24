from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

        # these are some min required fields for any metaclass
        