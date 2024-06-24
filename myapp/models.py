from django.db import models

# Create your models here.
class Guruh(models.Model):
    nomi = models.CharField(max_length=50)
    fakultet = models.CharField(max_length=50)
    
    
    def __str__(self) -> str:
        return self.nomi
    
    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural = 'Guruhlar'


class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    telefon_raqam = models.CharField(max_length=20)
    tugilgan_yili = models.DateField()
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.ism} {self.familya}"
    
    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"