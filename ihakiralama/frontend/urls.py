from django.urls import path
from . import views

urlpatterns = [#front-end urlleri
    path('', views.index, name="index"),#anasayfa urlsi
    path('ihalar/', views.iha_list, name="ihalar"),#ihalar urlsi
    path('kiralama/', views.kiralama_list, name="kiralama"),#kilamalar urlsi
    path('login/', views.user_login, name="log-in"),# kullanıcı giriş urlsi
    path('register/', views.user_register, name="sign-up"),#kullanıcı kayıt olma urlsi
    path('logout/', views.user_logout, name="log-out"),#kullanıcı çıkış urlsi
    # path('search/', views.search, name="search"),
]