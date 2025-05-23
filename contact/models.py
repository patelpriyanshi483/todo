from django.db import models
class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_number= models.TextField(max_length=10)


# Create your models here.
