from django.contrib import admin
from .models import Accounts, Employee, Member, Membership, Vehicle, Bill, Parking, Payment, Slot

class AccountsAdmin(admin.ModelAdmin):
    model = Accounts

@admin.register(Accounts,Employee, Member, Membership, Vehicle, Bill, Payment, Parking, Slot)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]