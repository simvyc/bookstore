from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'surname', 'username', 'last_login', 'is_active')
    list_display_links = ('email', 'name', 'surname')
    readonly_fields = ('last_login', 'is_admin', 'is_superadmin')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(Account, AccountAdmin)
