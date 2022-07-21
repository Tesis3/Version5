from django import forms
from socios.models import Socio
from django.conf.locale.en import formats as en_formats
#Formato de Fecha
en_formats.DATE_FORMAT = "%d/%m/%Y"

class SocioForm(forms.ModelForm):
    class Meta:
        model=Socio
        fields = ['nombre','apellido','email','telefono','fecha_nacimiento','dni']
        labels = {'nombre':"Nombre del Socio",
                  'apellido':"Apellido",
                  'email':"Email",
                  'telefono':"Telefono",
                  'fecha_nacimiento':"Fecha de Nacimiento",
                  'dni':"DNI"}
        widget = {'nombre':forms.TextInput(),
                  'apellido':forms.TextInput(),
                  'email':forms.TextInput(),
                  'telefono':forms.TextInput(),
                  'fecha_nacimiento':forms.DateField(),
                  'dni':forms.TextInput()}                
        help_texts = {'nombre':(),
                      'apellido':(),
                      'email':(),
                      'telefono':(),
                      'fecha_nacimiento':(),
                      'dni':(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })