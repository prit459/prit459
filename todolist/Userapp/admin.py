from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "password", "is_superuser", "is_staff","is_active","phone_number", )
    list_display = ("username", "email", "is_staff")
    list_filter =  ("is_staff" , "created_at","updated_at",)


admin.site.register(Contact)

admin.site.register(Task)