from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    title = models.CharField(max_length=255)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    content = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    experience = models.IntegerField(default=True)
    sort_number = models.IntegerField(default=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    sort_number = models.IntegerField(default=True)

    def __str__(self):
        return self.name
