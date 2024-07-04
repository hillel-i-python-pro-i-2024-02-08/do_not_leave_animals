from django.db import models


class Post(models.Model):
    """
    Model Form
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)



