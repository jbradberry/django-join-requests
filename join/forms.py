from django import forms
from models import JoinRequest

PENDING = JoinRequest.PENDING
WITHDRAWN = JoinRequest.WITHDRAWN
ACCEPTED = JoinRequest.ACCEPTED
REJECTED = JoinRequest.REJECTED


class JoinRequestForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ('message', 'state')

    DISALLOWED = {PENDING: (ACCEPTED, REJECTED),
                  WITHDRAWN: (ACCEPTED, REJECTED),
                  ACCEPTED: (PENDING, REJECTED),
                  REJECTED: (PENDING, WITHDRAWN, ACCEPTED)}

    DISALLOWED_MSG = {PENDING: "Your request has already been processed.",
                      WITHDRAWN: "You cannot alter a rejected request.",
                      ACCEPTED: "You cannot accept your own request."
                      REJECTED: "You cannot reject your own request."}

    def clean_state(self):
        if self.cleaned_data['state'] in DISALLOWED[self.initial['state']]:
            raise forms.ValidationError(
                DISALLOWED_MSG[self.cleaned_data['state']])


class JoinResponseForm(forms.ModelForm):
    class Meta:
        model = JoinRequest
        fields = ('response', 'state')

    DISALLOWED = {PENDING: (WITHDRAWN,),
                  WITHDRAWN: (PENDING, ACCEPTED, REJECTED),
                  ACCEPTED: (WITHDRAWN,),
                  REJECTED: (WITHDRAWN,)}

    DISALLOWED_MSG = {PENDING: "You cannot alter a withdrawn request.",
                      WITHDRAWN: "You cannot withdraw someone else's request.",
                      ACCEPTED: "You cannot accept a withdrawn request.",
                      REJECTED: "You cannot reject a withdrawn request."}

    def clean_state(self):
        if self.cleaned_data['state'] in DISALLOWED[self.initial['state']]:
            raise forms.ValidationError(
                DISALLOWED_MSG[self.cleaned_data['state']])
