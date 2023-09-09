from django.db import models
from hesaplar.models import CustomUser

# Create your models here.

class Iha(models.Model):
    marka = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
    agirlik = models.IntegerField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marka

class Kiralama(models.Model):
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE, related_name='ihalar')
    kiralayan_uye = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uyeler')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.kiralayan_uye.username}--->{self.iha.marka}'