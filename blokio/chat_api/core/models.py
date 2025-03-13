from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Messages(models.Model):
  message = models.CharField(max_length=120)
  
#new registration
class AccountManager(BaseUserManager):
  def create_user(self, email, username, password=None):
    if not email:
      raise ValueError('Please provide email')
    if not username:
      raise ValueError('username is required')
    
    user = self.model(email=self.normalize_email(email), username=username)

    user.set_password(password)
    user.save()

    return user
  
  def create_superUser(self, email, username, password):
    user = self.create_user(email = self.normalize_email(email), username = username, password = password)

    user.is_admin = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
class Account(AbstractBaseUser):
  email = models.EmailField(max_length=60, unique=True)
  username = models.CharField(max_length=255, unique=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  last_login_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ('username',)

  objects = AccountManager()

  def __str__(self) -> str:
    return self.username
  
  def has_perm(self, perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True

