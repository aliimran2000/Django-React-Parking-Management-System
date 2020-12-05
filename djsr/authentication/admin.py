from django.contrib import admin
from .models import Accounts

class AccountsAdmin(admin.ModelAdmin):
    model = Accounts

admin.site.register(Accounts, AccountsAdmin)