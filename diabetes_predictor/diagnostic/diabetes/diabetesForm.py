from django import forms
from ..models import *
from django.forms import ModelForm, widgets
from django.forms import Select

CHOICES = (
    ('Menos de 45 anos', 'Menos de 45 anos'),
    ('45-54 anos', '45-54 anos'),
    (' 55-64 anos', ' 55-64 anos'),
    (' Mais de 64 anos', ' Mais de 64 anos')
)

CHOICES_CINTURA = (
    ('Homens - Menos de 94 cm | Mulheres - Menos de 80 cm',
     'Homens - Menos de 94 cm | Mulheres - Menos de 80 cm'),
    ('Homens - 94-102 cm | Mulheres - 80-88 cm',
     'Homens - 94-102 cm | Mulheres - 80-88 cm'),
    ('Homens - Mais de 102 cm | Mulheres - Mais de 88 cm',
     'Homens - Mais de 102 cm | Mulheres - Mais de 88 cm'),
    ('Não sei', 'Não sei')
)

CHOICES_MEDICAMENTO = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)
CHOICES_ATIVIDADE = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)
CHOICES_GORDURA = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

CHOICES_FRUTAS = (
    ('Todos os dias', 'Todos os dias'),
    ('As vezes', 'As vezes'),
    ('Não como', 'Não como')
)

CHOICES_FAMILIA = (
    ('Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?',
     'Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?'),
    ('Sim: pais, irmãos, irmãs ou filhos', 'Sim: pais, irmãos, irmãs ou filhos'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

CHOICES_FUMAR = (
    ('Não', 'Não'),
    ('Fumava, mas parei', 'Fumava, mas parei'),
    ('Fumo 1 a 10 cigarros por dia', 'Fumo 1 a 10 cigarros por dia'),
    ('Fumo mais de 10 cigarros por dia', 'Fumo mais de 10 cigarros por dia')
)

CHOICES_ACUCAR = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

CHOICES_GLIC = (
    ('Não sei', 'Não sei'),
    ('S', 's')
)

CHOICES_LEVELGLIC = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

CHOICES_GIRL = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sou mulher', 'Não sou mulher'),
    ('Não sei', 'Não sei')
)

CHOICES_DIABETES = (
    ('Sim, diagnosticada pelo médico', 'Sim, diagnosticada pelo médico'),
    ('Não, de acordo com o meu médico', 'Não, de acordo com o meu médico'),
    ('Não sei', 'Não sei')
)


class Select(Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if not option.get('S'):
            option['attrs']['disabled'] = True

        if option.get('value') == 'S':
            option['attrs']['disabled'] = True

        return option


class DiabetesForm(forms.ModelForm):
    idade = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control my-component'}), initial=1)
    cintura = forms.ChoiceField(required=True, choices=CHOICES_CINTURA, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control my-component'}), initial=1)
    fruta = forms.ChoiceField(required=True, choices=CHOICES_FRUTAS, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    medicamento = forms.ChoiceField(required=True, choices=CHOICES_MEDICAMENTO, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    gordura = forms.ChoiceField(required=True, choices=CHOICES_GORDURA, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    atividade = forms.ChoiceField(required=True, choices=CHOICES_ATIVIDADE, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    familia = forms.ChoiceField(required=True, choices=CHOICES_FAMILIA, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    fumar = forms.ChoiceField(required=True, choices=CHOICES_FUMAR, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    acucar = forms.ChoiceField(required=True, choices=CHOICES_ACUCAR, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    glic = forms.ChoiceField(required=True, choices=CHOICES_GLIC, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    levelglic = forms.ChoiceField(required=True, choices=CHOICES_LEVELGLIC, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    ifgirl = forms.ChoiceField(required=True, choices=CHOICES_GIRL, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    diabetes = forms.ChoiceField(required=True, choices=CHOICES_DIABETES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)

    # email = forms.TextInput(required = True,widgets=forms.EmailField(attrs={'class': 'form-control'}), initial=1)

    class Meta():

        model = DiagnosticSample
        fields = ('sexo', 'idade', 'peso', 'altura',
                  'cintura', 'medicamento', 'glicemia')

        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'peso': forms.TextInput(attrs={'class': 'form-control'}),
            'altura': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.TextInput(attrs={'class': 'form-control'}),
            'glicemia': forms.TextInput(attrs={'class': 'form-control'})
        }
