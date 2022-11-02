from django.db import models
from account.models import Account


class Service(models.Model):
    title = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=50, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title

