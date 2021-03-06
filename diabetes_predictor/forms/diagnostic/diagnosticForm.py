from django import forms
from diagnostic.models import *
from django.forms import ModelForm, widgets
from django.forms import Select

#Diagnostic form
SEX_CHOICES = (
    ('Menos de 45 anos', 'Menos de 45 anos'),
    ('45-54 anos', '45-54 anos'),
    (' 55-64 anos', ' 55-64 anos'),
    (' Mais de 64 anos', ' Mais de 64 anos')
)

WEIST_CHOICES = (
    ('Homens - Menos de 94 cm | Mulheres - Menos de 80 cm',
     'Homens - Menos de 94 cm | Mulheres - Menos de 80 cm'),
    ('Homens - 94-102 cm | Mulheres - 80-88 cm',
     'Homens - 94-102 cm | Mulheres - 80-88 cm'),
    ('Homens - Mais de 102 cm | Mulheres - Mais de 88 cm',
     'Homens - Mais de 102 cm | Mulheres - Mais de 88 cm'),
    ('Não sei', 'Não sei')
)

MEDICINE_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

ACTIVITY_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

FATS_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

FRUITS_CHOICES = (
    ('Todos os dias', 'Todos os dias'),
    ('As vezes', 'As vezes'),
    ('Não como', 'Não como')
)

FAMILY_CHOICES = (
    ('Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?',
     'Sim: avós, tias, tios ou primos em 1º grau (excepto pais, irmãos, irmãs ou filhos)?'),
    ('Sim: pais, irmãos, irmãs ou filhos', 'Sim: pais, irmãos, irmãs ou filhos'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

SMOKE_CHOICES = (
    ('Não', 'Não'),
    ('Fumava, mas parei', 'Fumava, mas parei'),
    ('Fumo 1 a 10 cigarros por dia', 'Fumo 1 a 10 cigarros por dia'),
    ('Fumo mais de 10 cigarros por dia', 'Fumo mais de 10 cigarros por dia')
)

SUGAR_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

GLICEMY_LEVEL_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sei', 'Não sei')
)

GIRL_CHOICES = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
    ('Não sou mulher', 'Não sou mulher'),
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
    
    idade = forms.ChoiceField(required=True, choices=SEX_CHOICES, widget=forms.RadioSelect(attrs={'class': 'Radio' 'form-control my-component'}), initial=1)
    
    cintura = forms.ChoiceField(required=True, choices=WEIST_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control my-component'}), initial=1)
    
    fruta = forms.ChoiceField(required=True, choices=FRUITS_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    medicamento = forms.ChoiceField(required=True, choices=MEDICINE_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    gordura = forms.ChoiceField(required=True, choices=FATS_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    atividade = forms.ChoiceField(required=True, choices=ACTIVITY_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    familia = forms.ChoiceField(required=True, choices=FAMILY_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    fumar = forms.ChoiceField(required=True, choices=SMOKE_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    acucar = forms.ChoiceField(required=True, choices=SUGAR_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    levelglic = forms.ChoiceField(required=True, choices=GLICEMY_LEVEL_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)
    
    ifgirl = forms.ChoiceField(required=True, choices=GIRL_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'Radio' 'form-control'}), initial=1)

    # email = forms.TextInput(required = True,widgets=forms.EmailField(attrs={'class': 'form-control'}), initial=1)

    class Meta():

        model = DiagnosticSample
        fields = ('sexo', 'idade', 'peso', 'altura',
                  'cintura', 'medicamento', 'glicemia')

        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso', 'min': '8'}),
            'altura': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Altura'}),
            'glicemia': forms.TextInput(attrs={'class': 'form-control','placeholder':'Digite Não sei caso não saiba!'})
        }
