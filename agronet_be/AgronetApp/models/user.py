from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class userManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('El usuario no puede tener mas de un nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username = username,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.IntegerField('Num Doc de Identidad', unique=True, primary_key=True)
    name = models.CharField('Nombres', max_length=30)
    lastname = models.CharField('Apellidos', max_length=30)
    email = models.CharField('Correo electronico', max_length=100)
    address = models.CharField('Direccion', max_length=50)
    City = models.CharField('Ciudad', max_length=50)
    Department = models.CharField('Departamento', max_length=50)
    num_phone = models.IntegerField('Telefono')
    password = models.CharField('Contraseña', max_length=256)
    Type_sex = models.TextChoices('Femenino', 'Masculino')
    Type_rol = models.TextChoices('Comprador','Vendedor')
    sex = models.CharField(choices=Type_sex.choices, max_length=10)
    rol = models.CharField(blank=False, choices=Type_rol.choices, max_length=15)

    def save(self, **kwargs):
        some_salt = 'jjHgkjashflkjGJHA'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'