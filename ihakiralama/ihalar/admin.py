from django.contrib import admin
from ihalar.models import Iha, Kiralama
# Register your models here.
admin.site.register(Iha)#ihalar için admin kotrolü ekleme işlemi
admin.site.register(Kiralama)#kiralamalar için admin kotrolü ekleme
