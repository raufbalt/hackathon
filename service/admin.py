from django.contrib import admin

from service.models import Service, Category, Review

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Review)