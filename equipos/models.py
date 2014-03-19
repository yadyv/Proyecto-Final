from django.db import models

# Create your models here

class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreContinente)

class Equipo (models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)
    def __unicode__(self):
        return unicode(self.nombre)

class Posicion (models.Model):
    tipoPosicion = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.tipoPosicion)

class Jugador (models.Model):
    nombreJugador = models.CharField(max_length=50)
    posicion = models.ForeignKey(Posicion)
    equipo = models.ForeignKey(Equipo)
    estatura = models.FloatField(max_length=50)
    pieHabil = models.CharField(max_length=50)
    targetaAmarilla = models.IntegerField(max_length=50)
    targetaRoja = models.IntegerField(max_length=50)
    lesionado = models.CharField(max_length=50)
    titular = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
    fotos = models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.nombreJugador)

