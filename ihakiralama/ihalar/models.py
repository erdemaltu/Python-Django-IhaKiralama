from django.db import models
from hesaplar.models import CustomUser

# Create your models here.

class Iha(models.Model): #İha kayıtlarını tutacak tablo
    marka = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    kategori = models.CharField(max_length=120)
    agirlik = models.IntegerField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):#modelin nasıl temsil edileceği
        return self.marka

class Kiralama(models.Model): #Kiralama işlemlerini tutacak tablo
    iha = models.ForeignKey(Iha, on_delete=models.CASCADE, related_name='ihalar') #İha modeli ile bağlantı (iha verisi silindiğinde ona bağlı kiralamalarda silinir)
    kiralayan_uye = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uyeler') #Kullanıcılar ile bağlantı (kullanıcı verisi silindiğinde ona bağlı kiralamalarda silinir)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):#modelin nasıl temsil edileceği
        return f'{self.kiralayan_uye.username}--->{self.iha.marka}'