from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.name}"


