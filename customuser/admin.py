from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomerAppointments, User,Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(CustomerAppointments)