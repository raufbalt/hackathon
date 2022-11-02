from django.contrib import admin

from .cities import City
from .models import Account

admin.site.register(Account)
admin.site.register(City)
