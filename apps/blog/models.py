from django.db import models


class Post(models.Model):
    """
    Model Form
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)



