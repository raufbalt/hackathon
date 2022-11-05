from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=50)
    hour_from = models.CharField(max_length=10)
    hour_to = models.CharField(max_length=10)
    desc = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=10)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title



