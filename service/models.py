from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    title = models.CharField(max_length=30, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title



