from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

# ------------------ MODELOS ---------------------------
from django.contrib.auth.models import User
from rest_auth.registration.views import RegisterView

#-------------------VIEWS-------------------------------

class UserModelView(RegisterView):

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request':request})#Va a invocar a una clase de serializador
        serializer.is_valid(raise_exception=True)
        user = serializer.save(self.request)
        token, created = Token.objects.get_or_create(user=user)
        return Response(serializer.data)
        #response = ResponseJson("Error")
        # return Response('Error Formato')