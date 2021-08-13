from django.db import models

from escape_rooms.accounts_app.models import User


class Company(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.user.get_full_name()}"
