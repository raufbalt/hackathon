from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=50, null=True)
    hour_from = models.CharField(max_length=10, null=True)
    hour_to = models.CharField(max_length=10, null=True)
    desc = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=10, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.owner}'


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    marks = ((one, 'Too bad!'), (two, 'Bad!'), (three, 'Normal!'), (four, 'Good!'), (five, 'Excellent!'))


class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} -> {self.service}'


class Favorite(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = ['owner', 'service']

    def __str__(self):
        return f'{self.owner}`s favorites'




