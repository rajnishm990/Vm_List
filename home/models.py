from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
import os

def file_path(instance, filename):
    path = "documents/"
    format = "uploaded-"+filename
    return os.path.join(path, format)

class Appliances(models.Model):
    user = models.ForeignKey(
        User, related_name="admin", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    google_drive_link = models.CharField(max_length = 200 , null = True , blank = True)
    pdf_file = models.FileField(upload_to=file_path, null=True, blank=True , unique=False)
    description = models.TextField(max_length=500, null=True, blank=True)    
    
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
