from django import forms

class Button(forms.Form):
	buttonPressed = forms.CharField(required=True)