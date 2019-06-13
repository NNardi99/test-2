from django import forms
from .models import CustomUser

# class EmpleadoForm(forms.ModelForm):
#     cuil = forms.CharField()
#     telefono = forms.CharField()
#     domicilio = forms.CharField()
#     provincia = forms.InlineForeignKeyField()
#     localidad = forms.InlineForeignKeyField()

#     def clean(self):
#         cleaned_data = super().clean()
#         cuil = cleaned_data['cuil']
#         telefono = cleaned_data['telefono']
#         domicilio = cleaned_data['domicilio']
#         provincia = cleaned_data['provincia']
#         localidad = cleaned_data['localidad']

#     def __init__(self, *args, **kwargs):
#         super(EmpleadoForm, self).__init__(*args, **kwargs)
#         self.fields['cuil'].widget.attrs.update({'placeholder': 'xx-xxxxxxxx-x'})
#         self.fields['telefono'].widget.attrs.update({'placeholder': 'Ingrese el teléfono sin 0 ni 15'})

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['cuit'].widget.attrs.update({'placeholder': 'xx-xxxxxxxx-x'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Ingrese el teléfono sin 0 ni 15'})

class ProveedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['cuit'].widget.attrs.update({'placeholder': 'xx-xxxxxxxx-x'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Ingrese el teléfono sin 0 ni 15'})