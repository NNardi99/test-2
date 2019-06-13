from django import forms
from datetime import datetime, date
from administrador.models import Producto

class MyForm(forms.Form):
    fecha = forms.DateField(default=datetime.now)

    def clean(self):
        cleaned_data = super().clean()
        # Limitador de stock
        producto_id = cleaned_data.get("producto")
        cd_cantidad = cleaned_data.get("cantidad")
        product = Producto.objects.filter(id=producto_id).first()
        if not product:
            self.add_error('producto', "Seleccione un producto")
        if cd_cantidad>product.stockAct:
            self.add_error('cantidad', "La cantidad no debe superar el stock actual de {}".format(product.stockAct))
        
        # Limitador de fecha
        fecha = cleaned_data['fecha']
        if fecha > datetime.now():
            raise forms.ValidationError("La fecha no puede ser futuro!")
        return fecha