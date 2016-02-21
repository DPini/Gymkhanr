from django import forms

class ProvaCodiForm(forms.Form):
    CodiIntr = forms.CharField(label='Introdueix el codi', max_length=20)


class ProvaTestForm(forms.Form):
    def __init__(self, *args, **kwargs):
            idprova = kwargs.pop('idprova', None)
            super(ProvaTestForm, self).__init__(*args, **kwargs)
            from .models import RespostaTest
            self.fields['resposta'] = forms.ModelChoiceField(queryset=RespostaTest.objects.filter(idpregunta = idprova),empty_label= None)
    """class Meta:
        model = ProvaTest"""

"""
class ProvaTestForm(forms.Form):
    resp = forms.ModelChoiceField(label='Selecciona la resposta', queryset=None)
    def __init__(self, *args, **kwargs):
        resp = kwargs.pop('respostes')
        super(ProvaTestForm, self).__init__(*args, **kwargs)
        self.fields["resposta"] = forms.ModelChoiceField(queryset=resp)
"""
