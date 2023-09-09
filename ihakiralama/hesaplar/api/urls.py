from django.urls import path
from hesaplar.api import views as api_views

urlpatterns = [
    path('register/', api_views.register_user, name='register'),#kullanıcı oluşturma api urlsi
    path('login/', api_views.user_login, name='login'),#giriş yapma api urlsi
    path('logout/', api_views.user_logout, name='logout'),#çıkış yapma api urlsi
    path('uyeler/', api_views.uyeler, name='uyeler'),#kullanıcıların listesini görüntüleme api urlsi
]
