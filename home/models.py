from django.db import models
from django.utils import timezone

# Create your models here.
class GeneratedImages(models.Model):
    #id = models.BigAutoField(primary_key=True)
    img_name = models.CharField(blank=True, max_length=30)
    img = models.ImageField('Our Image',upload_to='images/')
