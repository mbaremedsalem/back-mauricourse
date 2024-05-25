from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .manager import UserManager
# Create your models here.
Role = (
    ('Admin', 'Admin'),
    ('Etudiante', 'Etudiante'),
    ('Enseignant', 'Enseignant'),
)


def image_upload_profile_agent(instance, filename):
    imagename, extension = filename.split(".")
    return "user/%s.%s" % (instance.id, extension)

class UserCourse(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(max_length=50, blank=True)
    prenom = models.CharField(max_length=50, blank=True)
    phone = models.CharField(unique=True, max_length=15)
    nni = models.CharField(unique=True, max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_upload_profile_agent, null=True, blank=True)
    number_attempt = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=30, choices=Role, null=True, default='Admin')
    transaction_authorization = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone or "N/A"  # support la langue arabe et français


Niveau = (
    ('Fondemental', 'Fondemental'),
    ('Breve', 'Breve'),
    ('Bac', 'Bac'),
)
Bac = (
        ('C', 'C'),
        ('D', 'D'),
        ('A', 'A'),
        ('O', 'O'),
)
# ------ Matiere -------    
class Matiere(models.Model):   
    titre=models.CharField(max_length=30,) 
    def __str__(self): 
        return self.titre 
    
# ------  Bac ----------
class Bacalorea(models.Model):
    niveau = models.CharField(max_length=30, choices=Bac, null=True, default='C')
    matieres = models.ManyToManyField(Matiere)
    def __str__(self): 
        return self.niveau 
    
#-------Etudiante-------------     
class Etudiante(UserCourse):
    bac = models.ForeignKey(Bacalorea, on_delete=models.CASCADE, null=True) 
    niveau_etude = models.CharField(max_length=30, choices=Niveau, null=True, default='Fondemental')
    # direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True) 
    def __str__(self): 
        return self.phone 
        

#-------Enseignant------------- 
class Enseignant(UserCourse):
    niveau_educatif =  models.CharField(max_length=30, choices=Niveau, null=True, default='Fondemental')
    # direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True) 

    def __str__(self): 
        return self.phone       

class Cour(models.Model):
    titre = models.CharField(max_length=100,null=True)
    date_commence_cour = models.DateTimeField()
    date_fin_cour = models.DateTimeField()
    prof = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True) 
