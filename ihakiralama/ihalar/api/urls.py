from django.urls import path
from ihalar.api import views as api_views

urlpatterns = [
    path('kiralama/', api_views.KiralamaListCreateAPIView.as_view(), name = 'kiralama-list'),
    path('kiralama/<int:pk>', api_views.KiralamaDetailAPIView.as_view(), name = 'kiralama-detail'),
    path('iha/', api_views.IhaListCreateAPIView.as_view(), name = 'iha-list'),
    path('iha/<int:pk>', api_views.IhaDetailAPIView.as_view(), name = 'iha-detail'),
]