from rest_framework import serializers
from ihalar.models import Iha, Kiralama
from hesaplar.api.serializers import UserSerializer

class IhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Iha
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']

class KiralamaSerializer(serializers.ModelSerializer):

    uyeler =  UserSerializer(many = True, read_only= True)

    # ihalar =  IhaSerializer(many = True, read_only= True)
    ihalar = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'iha-detail',
    )

    class Meta:
        model = Kiralama
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']