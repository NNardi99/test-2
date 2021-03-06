from django.contrib import admin
from administrador.models import (
    Provincia, Localidad, 
    CustomUser,
    Cliente, Proveedor, Categoria, Riesgo,
    Producto, Marca
)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from administrador.forms import ClienteForm, ProveedorForm
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch, cm
from reportlab.platypus import Table, TableStyle
import time

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id','provincia')
    search_fields = ('provincia',)

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('provincia','localidad')
    search_fields = ('localidad', 'provincia_id__provincia')

    # def has_change_permission(self, request, obj=None):
    #     return False

class MarcaAdmin(admin.ModelAdmin):
    ordering = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    # form = ProductoForm

    def stock_and_unity(obj):
        return "%s %s" % (obj.stockAct, obj.get_unidad_display())
    stock_and_unity.short_description = 'Stock disponible'

    list_display = ('id', 'image_tag', 'nombre', 'marca', 'categoria', 'riesgo', stock_and_unity)
    search_fields = ('nombre', 'categoria_id__nombre', 'marca_id__nombre')
    list_filter = ('categoria', 'riesgo', 'marca')
    ordering = ('id',)
    change_list_template = 'admin/change_list_graph_product.html'

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'descripcion': forms.Textarea}
        return super().get_form(request, obj, **kwargs)

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('nombre',)

class RiesgoAdmin(admin.ModelAdmin):
    ordering = ('riesgo',)

class CustomUserAdmin(UserAdmin):
    readonly_fields=('last_login','date_joined')  
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información Personal', {'fields': (
            'first_name', 
            'last_name', 
            'cuil', 
            'telefono', 
            'domicilio', 
            'provincia', 
            'localidad',
        )}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
            )
        }),
        ('Información Personal', {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'cuil',
                'telefono',
                'domicilio',
                'provincia',
                'localidad',
            )
        }),
        ('Permisos', {
            'classes': ('wide',),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        ('Fechas importantes', {
            'classes': ('wide',),
            'fields': ('date_joined',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.id:
            return super(CustomUserAdmin, self).get_readonly_fields(request, obj)
        else:
            return ('last_login',)
    
    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {
            'cuil': forms.TextInput(attrs={'placeholder': 'xx-xxxxxxxx-x', 'class': 'vTextField'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono sin 0 ni 15', 'class': 'vTextField'})
        }
        return super().get_form(request, obj, **kwargs)
    
    def change_active(self, request, queryset):
        for username in queryset:
            if username.is_active is True:
                username.is_active = False
                username.save()
            else:
                username.is_active = True
                username.save()
    change_active.short_description = 'Baja/Alta de Empleado'

    def export_tables_as_pdf(self, request, queryset):

        file_name = "table_entries{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)

        data = [['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login']]
        for d in queryset.all():
            item = [d.id, d.username, d.email, d.first_name, d.last_name, d.is_staff, d.is_active, d.last_login]
            data.append(item)

        doc = SimpleDocTemplate(response, pagesize=(21*inch, 29*inch))
        elements = []

        table_data = Table(data)
        table_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('BOX', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
                                        ("FONTSIZE",  (0, 0), (-1, -1), 13)]))
        elements.append(table_data)
        doc.build(elements)

        return response
    export_tables_as_pdf.short_description = "Exportar Tabla como PDF"

    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'groups')
    actions = [change_active, export_tables_as_pdf, ]
    ordering = ('id',)
    change_list_template = 'admin/change_list_graph_user.html'

class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm

    def change_active(self, request, queryset):
        for razon in queryset:
            if razon.activo is True:
                razon.activo = False
                razon.save()
            else:
                razon.activo = True
                razon.save()
    change_active.short_description = 'Baja/Alta de Cliente'

    list_display = ('id', 'razon', 'cuit', 'contacto', 'activo')
    search_fields = ('razon', 'cuit', 'contacto', 'localidad_id__localidad')
    list_filter = ('provincia', 'localidad', 'activo')
    actions = [change_active, ]
    ordering = ('id',)
    change_list_template = 'admin/change_list_graph_client.html'

class ProveedorAdmin(admin.ModelAdmin):
    form = ProveedorForm

    def change_active(self, request, queryset):
        for razon in queryset:
            if razon.activo is True:
                razon.activo = False
                razon.save()
            else:
                razon.activo = True
                razon.save()
    change_active.short_description = 'Baja/Alta de Proveedor'

    list_display = ('id', 'razon', 'cuit', 'contacto', 'activo')
    search_fields = ('razon', 'cuit', 'contacto', 'localidad_id__localidad')
    list_filter = ('provincia', 'localidad', 'activo')
    actions = [change_active, ]
    ordering = ('id',)
    change_list_template = 'admin/change_list_graph_client.html'

# Register your models here.

# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Riesgo, RiesgoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.disable_action('delete_selected') # Cant' use the action delete_select globally