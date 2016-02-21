from django import forms

class ProvaCodiForm(forms.Form):
    CodiIntr = forms.CharField(label='Introdueix el codi', max_length=20)
