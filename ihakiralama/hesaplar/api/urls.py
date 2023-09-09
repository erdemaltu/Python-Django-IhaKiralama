from django.urls import path
from hesaplar.api import views as api_views

urlpatterns = [
    path('register/', api_views.register_user, name='register'),
    path('login/', api_views.user_login, name='login'),
    path('logout/', api_views.user_logout, name='logout'),
    path('uyeler/', api_views.uyeler, name='uyeler'),
]
