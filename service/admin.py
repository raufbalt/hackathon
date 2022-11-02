from django.contrib import admin

from service.models import Service, Category, Subcategory

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Subcategory)