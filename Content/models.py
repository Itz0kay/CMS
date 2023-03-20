from django.db import models

# Create your models here.
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])

class Content(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.CharField(max_length=200, blank=False, null=False)
    summary = models.CharField(max_length=200, blank=False, null=False)
    document = models.FileField(upload_to=nameFile, blank=False, null=False)