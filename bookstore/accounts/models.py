from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, name, surname, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name or not surname:
            raise ValueError('Users must have a name and surname')
        
        email = self.normalize_email(email)
        username = name[:3].lower() + surname[:3].lower()  # First 3 letters of name + surname
        user = self.model(
            email=email,
            name=name,
            surname=surname,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, surname, email, password):
        user = self.create_user(
            name=name,
            surname=surname,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_superadmin = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return f'{self.name} {self.surname} ({self.username})'

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superadmin(self):
        return self.is_superadmin

class UserProfile():
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name    