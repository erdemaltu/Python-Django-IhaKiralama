from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ihalar.models import Iha, Kiralama
from ihalar.api.serializers import IhaSerializer, KiralamaSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class KiralamaListCreateAPIView(APIView):

    def get(self, request):
        kiralamalar = Kiralama.objects.all()
        serializer = KiralamaSerializer(kiralamalar, many=True, context = {'request':request})
        return Response(serializer.data)


    def post(self, request):
        serializer = KiralamaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class KiralamaDetailAPIView(APIView):

    def get_object(self, pk):
        kiralama_instance = get_object_or_404(Kiralama, pk=pk)
        return kiralama_instance

    def get(self, request, pk):
        kiralama = self.get_object(pk=pk)
        serializer = KiralamaSerializer(kiralama)
        return Response(serializer.data)

    def put(self, request, pk):
        kiralama = self.get_object(pk=pk)
        serializer = KiralamaSerializer(kiralama, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kiralama = self.get_object(pk=pk)
        kiralama.delete()
        return Response(status= status.HTTP_204_NO_CONTENT) 


class IhaListCreateAPIView(APIView):

    def get(self, request):
        ihalar = Iha.objects.all()
        serializer = IhaSerializer(ihalar, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = IhaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class IhaDetailAPIView(APIView):

    def get_object(self, pk):
        iha_instance = get_object_or_404(Iha, pk=pk)
        return iha_instance

    def get(self, request, pk):
        iha = self.get_object(pk=pk)
        serializer = IhaSerializer(iha)
        return Response(serializer.data)

    def put(self, request, pk):
        iha = self.get_object(pk=pk)
        serializer = IhaSerializer(iha, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        iha = self.get_object(pk=pk)
        iha.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)   