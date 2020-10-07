from django import forms
from datetime import datetime, date
import datetime
from administrador.models import Producto

class MyForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        # Limitador de stock
        product = cleaned_data.get("producto")
        cd_cantidad = cleaned_data.get("cantidad")

        if not product:
            self.add_error('producto', "Seleccione un producto")
        if cd_cantidad > product.stockAct:
            self.add_error('cantidad', "La cantidad no debe superar el stock actual de {}".format(product.stockAct))

class VentasForm(forms.ModelForm):
    fecha = forms.DateField(
        initial=date.today,
        widget=forms.SelectDateWidget(attrs = {
                 }, years = range(2018, datetime.date.today().year+1),),
    )
        # Limitador de fecha
    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser futuro!")