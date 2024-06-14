from django.db import models

# Create your models here.


class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)  # el campo puede                                                    
    username = models.CharField(max_length=30)
    # modulos = models.ManyToManyField('Modulo', through='Matricula')


    def __str__(self):
        return "%s - %s - %s" % (self.nombre,
                self.siglas,
                self.username)


class Jugador(models.Model):

    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)  # el campo puede                                                    
    numero_camiseta = models.IntField()
    sueldo = models.IntField()
    equipo = models.ForeignKey(Equipo, related_name='equipos')

    def __str__(self):
        return "%s - %s - %d - %d" % (self.nombre,
                self.posicion,
                self.numero_camiseta,
                self.sueldo)


class Campeonato(models.Model):

    nombre_campeonato = models.CharField(max_length=30)
    nombre_auspiciante = models.CharField(max_length=30)  # el campo puede                                                    

    def __str__(self):
        return "%s - %s" % (self.nombre_campeonato,
                self.nombre_auspiciante)


class CampeonatoEquipos(models.Model):
    """
    """
    anyo = models.CharField(max_length=30)
    equipo = models.ForeignKey(Equipo, related_name='equiposC')                                             
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatos')       

    def __str__(self):
        return "%s" % (self.anyo)