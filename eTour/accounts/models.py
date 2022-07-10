
from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class myAccountManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,username,contact,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("users must be provided")
        if not firstname:
            raise ValueError("Users must have their official names")
        if not lastname:
            raise ValueError("Users must have their official names")
        if not contact:
            raise ValueError("Users must have their functional phone numbers ")   

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            contact = contact

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,firstname,lastname,username,contact,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password= password,
            firstname = firstname,
            lastname = lastname,
            contact = contact

        ) 
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# phoneNumber = PhoneNumberField(unique=True)
class Accounts(AbstractBaseUser):
    firstname= models.CharField(max_length=150)
    lastname = models.CharField(max_length= 150)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    languages = models.CharField(max_length=250, null=True,blank=True)
    photo = models.ImageField(null=True,blank=True,upload_to='static')
    email = models.EmailField()
    contact = models.CharField(max_length=100,unique=True)
    username = models.CharField(max_length=100,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname','lastname','email','contact']

    objects = myAccountManager()

    # class Meta:
    #     verbose_name = ("User")
    #     verbose_name_plural = ("Users")
    def __str__(self) -> str:
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
