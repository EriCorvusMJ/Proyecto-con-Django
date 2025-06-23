from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    estatus = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username

class Bitacora(models.Model):
    id = models.AutoField(primary_key=True)
    movimiento = models.CharField(max_length=150)
    fecha = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')

    class Meta:
        db_table = 'bitacora'


""" class Task(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la tarea")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estatus = models.BooleanField(default=False, verbose_name="¿Terminada?")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return f"{self.nombre} - {'TERMINADA' if self.estatus else 'EN PROCESO'}" """