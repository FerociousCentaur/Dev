from django.contrib import admin

# Register your models here.
from .models import member, rovers

admin.site.register(member)
admin.site.register(rovers)