from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=HTMLField()
    slug=AutoSlugField(unique=True,populate_from="service_title",null=True,default=None)

# Create your models here.
