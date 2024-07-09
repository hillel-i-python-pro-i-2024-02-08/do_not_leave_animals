from django import forms
from apps.blog.models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating a post
    """

    class Meta:
        model = Post
        fields = ["title", "description", "photo"]
