from django.contrib import admin

from escape_rooms.accounts_app.models import Company, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
