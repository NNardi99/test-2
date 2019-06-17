from django.contrib import admin
from administrador.models import (
    Provincia, Localidad, 
    CustomUser,
    Cliente, Proveedor, Categoria,
    Producto
)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
# from administrador.forms import EmpleadoForm, ClienteForm, ProveedorForm
from administrador.forms import ClienteForm, ProveedorForm

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id','provincia')
    search_fields = ('provincia',)

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('provincia','localidad')
    search_fields = ('localidad', 'provincia_id__provincia')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'nombre', 'categoria', 'stockAct')
    search_fields = ('nombre', 'categoria_id__nombre')
    ordering = ('id',)

    def get_form(self, request, obj=None, **kwargs):
        kwargs['widgets'] = {'descripcion': forms.Textarea}
        return super().get_form(request, obj, **kwargs)

class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('nombre',)

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
    
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('id',)

class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm

    list_display = ('id', 'razon', 'cuit', 'contacto', 'activo')
    search_fields = ('razon', 'cuit', 'contacto')
    ordering = ('id',)

class ProveedorAdmin(admin.ModelAdmin):
    form = ProveedorForm

    list_display = ('id', 'razon', 'cuit', 'contacto', 'activo')
    search_fields = ('razon', 'cuit', 'contacto')
    ordering = ('id',)

# Register your models here.

# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)