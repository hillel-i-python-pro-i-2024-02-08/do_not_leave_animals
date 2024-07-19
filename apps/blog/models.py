from django.db import models


class Post(models.Model):
    """
    Model Form
    """

    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/blog", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
