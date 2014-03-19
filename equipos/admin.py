from django.contrib import admin
from models import Equipo, Continente, Jugador, Posicion
# Register your models here.

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre','continente','tecnico')
    search_fields = ('nombre','continente__nombreContinente','tecnico',)
    list_filter = ('continente',)

class ContinenteAdmin(admin.ModelAdmin):
    list_display=('nombreContinente',)

class PosicionAdmin(admin.ModelAdmin):
    list_display=('tipoPosicion',)

class JugadorAdmin(admin.ModelAdmin):
    list_display=('nombreJugador','posicion','equipo','estatura','pieHabil','targetaAmarilla','targetaRoja','lesionado','titular','goles','fotos',)
    search_fields = ('nombreJugador',)

admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Continente,ContinenteAdmin)
admin.site.register(Jugador,JugadorAdmin)
admin.site.register(Posicion,PosicionAdmin)
