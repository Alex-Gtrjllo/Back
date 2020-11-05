from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# ------------------ MODELOS ---------------------------
from Profile.models import ProfileModel, ProfileUser

#-------------------SERIALIZERS-------------------------
from Profile.serializers import ProfileModelSerializers, ProfileUserSerializers

#-------------------VIEWS-------------------------------
class ProfileModelView(APIView):

    def post(self, request, format=None):
        serializer = ProfileModelSerializers(data=request.data, context={'request':request})#Va a invocar a una clase de serializador
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        #response = ResponseJson("Error")
        return Response('Error Formato')

class ProfileUserView(APIView):

    def post(self, request, format=None):
        serializer = ProfileUserSerializers(data=request.data, context={'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        #response = ResponseJson("Error")
        return Response('Error Formato')

    def get(self, request, format=None):
        users = ProfileUser.objects.all()
        serializer = ProfileUserSerializers(users, many=True)
        return Response(serializer.data)

class ProfileUserMethods(APIView):        

    def get_object(self, pk):
        try:
            return ProfileUser.objects.get(pk=pk)
        except ProfileUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ProfileUser = self.get_object(pk)
        serializer = ProfileUserSerializers(ProfileUser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ProfileUser = self.get_object(pk)
        serializer = ProfileUserSerializers(ProfileUser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ProfileUser = self.get_object(pk)
        ProfileUser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)