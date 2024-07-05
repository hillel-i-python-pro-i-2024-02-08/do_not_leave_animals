from django.db import models


class Post(models.Model):
    """
    Model Form
    """
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=4000)
    date = models.DateTimeField(auto_now=True)



