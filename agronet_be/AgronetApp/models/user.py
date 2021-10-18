from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password

class userManager(BaseUserManager):
    def create_user(self, usersname, password=None):
        if not usersname:
            raise ValueError('El usuario no puede tener mas de un nombre de usuario')
        user = self.model(usersname=usersname)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, usersname, password):
        user = self.create_user(
            username = usersname,
            password = password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    usersname = models.IntegerField('Num Doc de Identidad', primary_key=True)
    name_user = models.CharField('Nombres', max_length=30)
    lastname_user = models.CharField('Apellidos', max_length=30)
    email = models.CharField('Correo electronico', max_length=100)
    address_user = models.CharField('Direccion', max_length=50)
    id_city = models.ForeignKey(city,related_name='ciudad',null=False,on_delete=models.CASCADE)
    id_department = models.ForeignKey(Departament,related_name='departamento',null=False,on_delete=models.CASCADE)
    num_phone = models.IntegerField('Telefono')
    password = models.CharField('Contraseña', max_length=256)
    Type_sex = models.TextChoices('Femenino', 'Masculino')
    Type_rol = models.TextChoices('Comprador','Vendedor')
    sex_user = models.CharField(choices=Type_sex.choices, max_length=10)
    rol_user = models.CharField(blank=False, choices=Type_rol.choices, max_length=15)

    def save(self, **kwargs):
        some_salt = 'jjHgkjashflkjGJHA'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'usersname'
