from django.contrib import admin

from .cities import City
from .models import Account, Spam_Contacts

admin.site.register(Account)
admin.site.register(City)
admin.site.register(Spam_Contacts)
