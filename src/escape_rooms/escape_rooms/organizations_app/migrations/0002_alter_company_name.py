# Generated by Django 3.2.5 on 2021-08-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
