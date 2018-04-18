from django import forms

class NameForm(forms.Form):
    sort_hot = forms.BooleanField(required=False)
