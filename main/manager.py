from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        if not phone_number:
            raise ValueError("user must have a phone number")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )

        extra_fields.setdefault('is_active', True),
        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_superuser', False),

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, phone_number,  password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        if not phone_number:
            raise ValueError("user must have a phone number")

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )

        '''
        extra_fields.setdefault('is_active', True):
        This line of code uses the setdefault() method of a dictionary (extra_fields) to set a default value for the key 'is_active' if it doesn't already exist in the dictionary. If the key 'is_active' is already present in the dictionary, this line of code will have no effect on its value. If the key is not present, it will add 'is_active': True to the dictionary.
        '''

        extra_fields.setdefault('is_active', True),
        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_superuser', True),

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff status True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser status True')

        '''
        user.is_active = extra_fields.get('is_active'):
        This line of code assigns the value associated with the key 'is_active' from the extra_fields dictionary to the is_active attribute of the user object. It uses the get() method of the dictionary to retrieve the value. If the key 'is_active' is not present in the extra_fields dictionary, extra_fields.get('is_active') will return None, and the user.is_active attribute will also be set to None.
        '''

        user.is_active = extra_fields.get('is_active')
        user.is_staff = extra_fields.get('is_staff')
        user.is_superuser = extra_fields.get('is_superuser')

        user.set_password(password)
        user.save()
        return user
