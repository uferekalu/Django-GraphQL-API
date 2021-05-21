from django.db import models
from django.utils.text import slugify

from uuid import uuid4

# Create your models here.

def image_upload(instance, filename):
	basename, file_extension = filename.split(".")
	return f"IMGIDPROJ-{uuid4().hex}.{file_extension}"


class Image(models.Model):
    uuid = models.CharField(max_length=120)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.uuid
    
    class Meta:
        ordering = ('uuid',)