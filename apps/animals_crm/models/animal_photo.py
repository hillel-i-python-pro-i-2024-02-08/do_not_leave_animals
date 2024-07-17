from django.db import models
from ulid import new


def get_animal_avatar_path(
    instance,  # noqa: ANN001, ARG001
    filename: str,
) -> str:
    filename_part, extension = filename.rsplit(".", maxsplit=1)

    unique_part = new().uuid.hex

    return f"photos/crm/{unique_part}/{filename_part}.{extension}"


class AnimalPhoto(models.Model):
    """..."""

    animal = models.ForeignKey(
        "AnimalCard",
        on_delete=models.CASCADE,
        related_name="photos",
    )

    image = models.ImageField(upload_to=get_animal_avatar_path, null=False, blank=False, default="photos/default.jpg")

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.animal.name} photo"
