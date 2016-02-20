from django.db import models

# Create your models here.
class Gymcana(models.Model) :
     nom = models.CharField(max_length = 20)
     descripcio=models.TextField()
     def __str__(self):
            return self.nom

class Prova(models.Model) :
     numgym = models.ForeignKey(Gymcana)
     nom = models.CharField(max_length = 20)
     descripcio=models.TextField()
     superada = models.BooleanField()
     def __str__(self):
            return self.nom


class ProvaTest(Prova):
    respostacorrecta = models.IntegerField()

class RespostaTest(models.Model):
    idpregunta = models.ForeignKey(ProvaTest)
    resposta = models.CharField(max_length = 50)

class ProvaCodi(Prova):
    codi = models.CharField(max_length = 20)
