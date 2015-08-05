from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    first = models.CharField(max_length=255)
    second = models.CharField(max_length=255)
    image = models.ImageField(upload_to="photos/")

    def __str__(self):
        return str(self.image)
