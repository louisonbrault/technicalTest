from django.forms import ModelForm
from django import forms
from .models import Room, Reservation
from django.contrib.admin import widgets

class ReservationForm(ModelForm):
     class Meta:
         model = Reservation
         fields = ('room', 'startTime', 'endTime','reason')

     def __init__(self, *args, **kwargs):
         super(ReservationForm, self).__init__(*args, **kwargs)
         self.queryset = forms.ModelChoiceField(queryset=Room)
