from django.db import models


class AnimalComment(models.Model):
    """..."""

    animal = models.ForeignKey(to="AnimalCard", on_delete=models.CASCADE, related_name="comments")

    comment_text = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if len(self.comment_text) > 20:
            return f"{self.comment_text[:20]}..."
        else:
            return self.comment_text
