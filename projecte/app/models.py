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
    pass 

class ProvaCodi(Prova):
    pass 
