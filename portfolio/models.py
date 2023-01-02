from django.db import models
from django.db.models import fields

# Create your models here.
class Project(models.Model):
    title = fields.CharField(max_length=50)
    description = fields.CharField(max_length=255)
    image = models.ImageField(upload_to="portfolio/images/")
    url = fields.URLField(blank=True)