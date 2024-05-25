from .models import *
from rest_framework import serializers 
from django.contrib.auth import authenticate

#--------------login---------------------
class MyTokenObtainPairSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active and not user.is_blocked:
            user.number_attempt=0
            user.save()
            return user
        
        elif user and user.is_active and user.is_blocked:
            # return Response('message')
            # return Response(serializers.errors)
            raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur'})
        
        try:
            obj= UserCourse.objects.get(phone=data['phone'])
            print(obj.number_attempt)
            if obj.number_attempt<5:
                obj.number_attempt +=1
                print(obj.number_attempt)
                obj.save()
                raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur.'})
            else:
                obj.number_attempt +=1
                print(obj.number_attempt)
                obj.is_blocked=True
                obj.save()
                raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur.'})
        except:
            raise serializers.ValidationError({'message':'Informations invalides.'})
         
#------ register etudiant ---------        
class RegisterEtudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiante
        fields =  ('nom','prenom','phone','nni','email','address','image','role','bac','password','niveau_etude')
        extra_kwargs = {
            'password': {'write_only': True}
        }        
#------ register enseignant ---------
class RegisterEnseignantserializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields =  ('nom','prenom','phone','nni','email','address','image','role','password','niveau_educatif')
        extra_kwargs = {
            'password': {'write_only': True}
        }  
