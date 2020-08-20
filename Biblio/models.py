from django.db import models

# Create your models here.
class Material(models.Model):
    autor = models.CharField(max_length=50, default="")
    titulo = models.CharField(max_length=50, default="")
    anio = models.IntegerField(null = True)
    status = models.BooleanField(null = True)

    def __str__(self):
        return str(self.titulo)
    
    status.boolean = True

class Libro(Material):
    editorial = models.CharField(max_length=50, default="")
    portada = models.ImageField(null = True)

class Revista(Material):
    numero = models.IntegerField(null = True)

class TipoMaterial(models.Model):
    libro = models.ForeignKey(Libro, null = True, default = None, on_delete=models.CASCADE)
    revista = models.ForeignKey(Revista, null = True, default = None, on_delete=models.CASCADE)

class Persona(models.Model):
    nombre = models.CharField(max_length=50, default="")
    apellido = models.CharField(max_length=50, default="")
    correo = models.CharField(max_length=50, default="")
    telefono = models.IntegerField(null = True)
    numLibros = models.IntegerField(null=True)
    adeudo = models.FloatField(null = True)

    def __str__(self):
        return str(self.nombre + " " + self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField(null = True)

class Profesor(Persona):
    numEmpleado = models.IntegerField(null = True)

class TipoPersona(models.Model):
    alumno = models.ForeignKey('Alumno', null = True, default = None, on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', null = True, default = None, on_delete=models.CASCADE)

class Prestamo(models.Model):
    persona = models.ForeignKey( 'Persona', on_delete=models.CASCADE, null = True, default = None)
    material = models.ForeignKey('Material', on_delete=models.CASCADE, null = True, default = None)
    fechaSalida = models.DateField(auto_now=True)
    fechaRegreso = models.DateField()

    def __str__(self):
        return str(self.persona.nombre + "--" + self.material.titulo)


