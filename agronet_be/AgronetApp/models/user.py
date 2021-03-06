from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.contrib.auth.hashers import make_password
from AgronetApp.models.city import City

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
    id = models.IntegerField(primary_key=True)
    usersname = models.CharField('Username', max_length=100)
    name_user = models.CharField('Nombres', max_length=30)
    lastname_user = models.CharField('Apellidos', max_length=30)
    email = models.CharField('Correo electronico', max_length=100)
    address_user = models.CharField('Dirección', max_length=50)
    id_city = models.ForeignKey(City,related_name='ciudad',null=False,on_delete=models.CASCADE)
    num_phone = models.IntegerField('Telefono')
    password = models.CharField('Contraseña', max_length=256)
    #Type_sex = [("Masculino","MASCULINO"),("Femenino","FEMENINO")]
    #Type_rol = models.TextChoices(("Comprador","Comprador"),("Vendedor","Vendedor"))
    sex_user = models.CharField('Sexo', max_length=10)
    rol_user = models.CharField('Rol', max_length=15)

    def save(self, **kwargs):
        some_salt = 'jjHgkjashflkjGJHA'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'id'
    def __str__(self):
        return str(self.id)
