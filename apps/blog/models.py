from django.db import models


class Post(models.Model):
    """
    Model Form
    """
    title = models.CharField(max_length=60)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/blog', default="photos/default.jpg")
    date = models.DateTimeField(auto_now_add=True)



