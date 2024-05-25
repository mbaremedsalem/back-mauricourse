from django.shortcuts import render
from .serializer import *
from rest_framework.exceptions import ValidationError,APIException
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

#-------------------login---------------------
class InvalidInformationException(APIException):
    status_code = 400
    default_detail = 'Informations invalides'

class MytokenManager(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({
            'message': 'Information invalide',
            'status':status.HTTP_400_BAD_REQUEST, 
        })

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        image_url = user.image.url if user.image else None
        
        return Response({
                'message': 'login success',
                'status': status.HTTP_200_OK, 
                'role': user.role,
                'access': str(refresh.access_token),
                'refresh_token': str(refresh),  
            })

#----------------- Register --------------    
class RegisterAPI(TokenObtainPairView):
    serializer_classes = {
        'Etudiante': RegisterEtudianteSerializer,
        'Enseignant': RegisterEnseignantserializer,
    }

    def get_serializer_class(self):
        role = self.request.data.get('role', False)
        serializer_class = self.serializer_classes.get(role)
        return serializer_class

    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone', False)
        password = request.data.get('password', False)
        role = request.data.get('role', False)

        if phone and password and role:
            serializer_class = self.get_serializer_class()
            if serializer_class is None:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Invalid role'})

            serializer = serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            try:
                user = serializer.save()
                user.set_password(password)
                user.save()
                refresh = RefreshToken.for_user(user)

                return Response({
                    'message': 'Register success',
                    'status': status.HTTP_200_OK, 
     
                })
            except:
                return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Bad request'})

        return Response({'status': status.HTTP_400_BAD_REQUEST, 'Message': 'Envoyez le numéro de telephone exist'})
