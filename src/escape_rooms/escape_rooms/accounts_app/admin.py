from django.contrib import admin

from escape_rooms.accounts_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
