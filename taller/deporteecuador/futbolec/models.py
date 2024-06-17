from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, self.siglas, self.username)

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero_camiseta = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(Equipo, related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %d" % (self.nombre, self.posicion, self.numero_camiseta, self.sueldo)

class Campeonato(models.Model):
    nombre_campeonato = models.CharField(max_length=30)
    nombre_auspiciante = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.nombre_campeonato, self.nombre_auspiciante)

class CampeonatoEquipos(models.Model):
    anyo = models.CharField(max_length=30)
    equipo = models.ForeignKey(Equipo, related_name='campeonatos', on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='equipos', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.anyo)
