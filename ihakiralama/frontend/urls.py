from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ihalar/', views.iha_list, name="ihalar"),
    path('kiralama/', views.kiralama_list, name="kiralama"),
    path('login/', views.user_login, name="log-in"),
    path('register/', views.user_register, name="sign-up"),
    path('logout/', views.user_logout, name="log-out"),
    # path('search/', views.search, name="search"),
]