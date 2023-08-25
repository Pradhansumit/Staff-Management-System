from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import *

USER_STATUS_CHOICE = (
    ("admin", "Admin"),
    ("staff", "Staff"),
)


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.IntegerField()
    user_status = models.CharField(
        max_length=10, choices=USER_STATUS_CHOICE, default='staff')
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['phone_number']

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

# update user time-sheet by clicking on the start and stop button from timer frontend page

# start time


class StartTime(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)


# stoptime
class StopTime(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    stop_time = models.DateTimeField(auto_now_add=True)


class TimeSheet(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    start_time = models.ForeignKey(StartTime, on_delete=models.PROTECT)
    stop_time = models.ForeignKey(StopTime, on_delete=models.PROTECT)
