from django import forms
from .models import Gym
#DataFlair
class GymCreate(forms.ModelForm):
    class Meta:
        model = Gym
        fields = '__all__'