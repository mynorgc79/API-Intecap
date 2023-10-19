from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, dpi, nombre,apellido, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        
        email = self.normalize_email(email)
        usuario = self.model(
            email=email,
            dpi=dpi,
            nombre=nombre,
            apellido=apellido,
            password=password,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, dpi, nombre,apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, dpi, nombre,apellido, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellido= models.CharField(max_length=255)
    dpi = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    
    objects = CustomUserManager()
    class Meta:
        ordering = ['-created_at']
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellido',  'dpi']

    def has_perm(self, perm, obj=None):
        # Define aquí tu lógica para los permisos
        return True

    def has_module_perms(self, app_label):
        # Define aquí tu lógica para los permisos de módulo
        return True
