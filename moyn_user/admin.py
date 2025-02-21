from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MoynUser

class MoynUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'profile_url')}),
    )

admin.site.register(MoynUser, MoynUserAdmin)