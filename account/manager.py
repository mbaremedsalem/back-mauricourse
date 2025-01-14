from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    def _create_user(self,phone, password, **extra_fields):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone:
            raise ValueError('The given phone must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)
    
    def create_etutiant(self, nom,prenom,email,address,phone, password, **other_fields):
        other_fields.setdefault('role', 'Etudiante')
        user = self.model(nom=nom,phone=phone,  prenom=prenom,
                          email=email, address=address, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_staffuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staff User must have is_staff=True.')

        return self._create_user(username, password, **extra_fields)