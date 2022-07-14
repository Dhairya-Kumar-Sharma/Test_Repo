from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import ClientRequest

@admin.register(ClientRequest)
class ClientRequestAdmin(UserAdmin):
    
    search_fields = ('url', 'profile',)
    ordering = ('profile',)
    list_display = ('profile', 'username', 'url', 'code_link', 'token', 'version_control', 'branch')
    list_filter = ('url', 'code_link', 'profile', )
    filter_horizontal =  tuple()
    
    fieldsets = (
        ('Client Details', {'fields': ('profile', 'username',)}),
        ('Code Details', {'fields': ('url', 'code_link', 'token', 'version_control', 'branch')}),
    )
