from django.db import models

class Partida(models.Model):  # Substituindo o nome de Estatistica por Partida
    time_casa = models.CharField(max_length=100, verbose_name="Time da Casa")
    time_visitante = models.CharField(max_length=100, verbose_name="Time Visitante")
    gols_casa = models.IntegerField(verbose_name="Gols do Time da Casa")
    gols_visitante = models.IntegerField(verbose_name="Gols do Time Visitante")
    data_partida = models.DateField(verbose_name="Data da Partida")

    def __str__(self):
        return f"{self.time_casa} ({self.gols_casa}) x ({self.gols_visitante}) {self.time_visitante} - {self.data_partida}"
