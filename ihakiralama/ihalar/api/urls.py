from django.urls import path
from ihalar.api import views as api_views

urlpatterns = [
    path('kiralama/', api_views.KiralamaListCreateAPIView.as_view(), name = 'kiralama-list'),#kiramaların api urlsi
    path('kiralama/<int:pk>', api_views.KiralamaDetailAPIView.as_view(), name = 'kiralama-detail'),#her kiramanın tek sorgusu için api urlsi
    path('iha/', api_views.IhaListCreateAPIView.as_view(), name = 'iha-list'),#ihaların api urlsi
    path('iha/<int:pk>', api_views.IhaDetailAPIView.as_view(), name = 'iha-detail'),#her ihanın tek sorgusu için api urlsi
]