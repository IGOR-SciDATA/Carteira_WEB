from django.forms import ModelForm
from django import forms
import CarteiraApp.models as Models
from CarteiraWeb.settings import DATE_INPUT_FORMATS as databr

# Create your forms here
class FormCliente(ModelForm):
   data_nascimento = forms.DateField(input_formats=databr)
   class Meta:
        model = Models.Cliente
        fields = ['__all__']