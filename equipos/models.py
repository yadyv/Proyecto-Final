from django.db import models

  # Create your models here
POSICIONES = (
    ('seleccione','Seleccione'),
    ('arquero','Arquero'),
    ('defensa','Defensa'),
    ('volante','Volante'),
    ('delantero','Delantero'),
)

PIEHABIL = (
    ('seleccione','Seleccione'),
    ('derecha','Derecha'),
    ('izquierda','Izquierda'),
)

LESIONADO = (
    ('seleccione','Seleccione'),
    ('si','Si'),
    ('no','No'),
)

TITULAR = (
    ('seleccione','Seleccione'),
    ('si','Si'),
    ('no','No'),
)

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

class Jugador (models.Model):
    nombreJugador = models.CharField(max_length=50)
    posicion = models.CharField(choices=POSICIONES, default='seleccione', max_length=10)
    equipo = models.ForeignKey(Equipo)
    estatura = models.FloatField(max_length=50)
    pieHabil = models.CharField(choices=PIEHABIL, default='seleccione', max_length=10)
    targetaAmarilla = models.IntegerField(max_length=50)
    targetaRoja = models.IntegerField(max_length=50)
    lesionado = models.CharField(choices=LESIONADO, default='seleccione', max_length=10)
    titular = models.CharField(choices=TITULAR, default='seleccione', max_length=10)
    goles = models.CharField(max_length=50)
    fotos = models.ImageField(upload_to='images',verbose_name='foto', null=True,)
    def __unicode__(self):
        return unicode(self.nombreJugador
)

