from django import forms
from .models import CustomUser

# class EmpleadoForm(forms.ModelForm):
#     cuil = forms.CharField()
#     telefono = forms.CharField()

#     def clean(self):
#         cleaned_data = super().clean()
#         cuil = cleaned_data['cuil']
#         telefono = cleaned_data['telefono']

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