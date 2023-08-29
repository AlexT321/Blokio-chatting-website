from django.contrib import admin
from .models import Messages
from .models import Account


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
  list_display = ('email', 'password')
admin.site.register(Messages)
admin.site.register(Account ,CustomUserAdmin)