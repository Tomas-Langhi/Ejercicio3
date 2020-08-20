from django.contrib import admin
from Biblio.models import *

class TipoMaterialInline(admin.TabularInline):
    model = TipoMaterial

class RevistaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'numero','status',]
    inlines = [TipoMaterialInline, ]

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'editorial','status',]
    inlines = [TipoMaterialInline, ]

class TipoPersonaInline(admin.TabularInline):
    model = TipoPersona

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'matricula','adeudo', 'numLibros',]
    inlines = [TipoPersonaInline,]

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'numEmpleado','adeudo', 'numLibros',]
    inlines = [TipoPersonaInline,]

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['persona', 'material', 'fechaSalida', 'fechaRegreso']


# Register your models here.

admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Prestamo, PrestamoAdmin)







