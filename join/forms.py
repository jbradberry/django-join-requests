from django import forms
from models import JoinRequest


class JoinHostForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ('host_message', 'host_state')


class JoinUserForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ('message', 'state')
