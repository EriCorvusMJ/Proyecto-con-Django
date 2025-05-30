from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True)  # Opcional, Django lo crea automáticamente si no lo defines
    username = models.CharField(max_length=50, unique=True)  # Recomiendo que username sea único
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)  # Recomiendo email único para evitar duplicados
    photo = models.ImageField(upload_to='photos/')

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.username


class Bitacora(models.Model):
    id = models.AutoField(primary_key=True)  # También opcional, Django lo crea solo
    movimiento = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)  # Guarda fecha y hora al crear

    class Meta:
        db_table = 'bitacora'

    def __str__(self):
        return f"{self.movimiento} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
