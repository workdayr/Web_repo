from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from Web_repo.models.product import Products

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=256, null=False, blank=False)
    first_name = models.CharField(max_length=35, null=False)
    last_name = models.CharField(max_length=35,  null=True, blank=True)
    state = models.CharField(max_length=20, null=False, default='Unknown')
    date_of_birth = models.DateField(null= True, blank=True, default="2000-01-01")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    general_notifications_enabled = models.BooleanField(default=True)
    # Inherited from PermissionsMixin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username



class UserActivity(models.Model):
    user_activity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    last_login = models.DateTimeField(null=True, blank=True, default=None)
    ip_address = models.CharField(max_length=50, null=False)
    state = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.last_login if self.last_login else 'Nunca ha iniciado sesión'}"


class UserFavorites(models.Model):
    user_favorites_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="likes")
    liked_at = models.DateTimeField(auto_now_add=True)
    active_notifications = models.BooleanField(default=True)
    price_threshold = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage_threshold = models.IntegerField(default=10)

    class Meta:
        unique_together = ('user_id', 'product_id')