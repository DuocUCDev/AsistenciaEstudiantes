from django.db import models

# Create your models here.
class Estudiante(models.Model):
    GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    rut = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO)
    
    def __str__(self):
        return f"{self.rut} : {self.nombre} {self.apellido}"

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.codigo} : {self.nombre}"

class Seccion(models.Model):
    JORNADA = [
        ('D', 'Diurna'),
        ('V', 'Vespertina'),
    ]
    nombre = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    jornada = models.CharField(max_length=1, choices=JORNADA)
    
    def __str__(self) -> str:
        return f"{self.curso.codigo}-{self.nombre}"

class Asistencia(models.Model):
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField()
    presente = models.BooleanField()
    
    def __str__(self):
        return f"{self.seccion} : {self.estudiante} : {self.presente}"