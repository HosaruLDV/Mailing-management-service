from django.contrib import admin
from djank.models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'middle_name', 'comment',)