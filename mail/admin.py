from django.contrib import admin
from .models import Mail

# Register your models here.

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    pass