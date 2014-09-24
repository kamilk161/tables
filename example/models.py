from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)