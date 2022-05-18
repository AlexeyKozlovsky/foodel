from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import UserManager

# from users.models import Employee, Businessman, Courier


class BaseUserManager(UserManager):
    def create_user(self, email=None, password=None, phone=None, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        if password is None:
            raise TypeError('Users must have a password')
        if phone is None:
            raise TypeError('Users must have a phone')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email=None, password=None, phone=None, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password, phone)
        user.is_superuser = True
        user.save()

        return user


class BaseUser(AbstractBaseUser):
    """Модель, характеризующая базового абстрактного пользователя,
    от которого наследуются пользователи всех других ролей"""

    objects = BaseUserManager()
    user_id = models.AutoField(primary_key=True)

    email = models.EmailField(max_length=127, unique=True, null=False, default='tilt@ya.ru')
    phone = models.CharField(max_length=15, unique=True, null=False, default='89999999999')
    first_name = models.CharField(max_length=127, null=True, default='Tilt')
    last_name = models.CharField(max_length=127, null=True, default='Tilt')
    birthday = models.DateField(null=True, blank=True)
    img = models.ImageField(default='images/users/default.jpg', upload_to='images/users')

    # rating = models.OneToOneField('rating.Rating', null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    class Meta:
        app_label = 'core'
        db_table = 'user'

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
