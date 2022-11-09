from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True!')
        return self._create_user(email, password, **kwargs)


class AccountCategory(models.Model):
    one = 1
    two = 2
    choice = ((one, 'client'), (two, 'executor'))


class Account(AbstractUser):
    email = models.EmailField('email address', unique=True)
    activation_code = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)

    status = models.PositiveSmallIntegerField(choices=AccountCategory.choice, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_(
                                        'Designates whether this user should be treated as active.' 
                                        'Unselect this  instead of deleting accounts.'))
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    username = models.CharField(max_length=100, default=0, unique=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code


#  ДЛЯ ТОГО ЧТОБЫ ОТПРАВИТЬ ПИСЬМО СПАМ
class Spam_Contacts(models.Model):
    email = models.EmailField('email address', unique=True)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Спам почта'
        verbose_name_plural = 'Адреса для спама'
