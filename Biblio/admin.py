from django.contrib import admin
from Biblio.models import *

# Register your models here.
admin.site.register(Libro,)
admin.site.register(Revista,)
admin.site.register(Alumno,)
admin.site.register(Profesor,)
admin.site.register(Prestamo,)