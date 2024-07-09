# noinspection PyPackageRequirements
import ulid
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_animal_avatar_path(
    instance,  # noqa: ANN001, ARG001
    filename: str,
) -> str:
    filename_part, extension = filename.rsplit(".", maxsplit=1)

    uuid_from_ulid = ulid.new().uuid.hex

    return f"photos/crm/{uuid_from_ulid}/file.{extension}"


class AnimalPhoto(models.Model):
    """..."""

    animal = models.ForeignKey(
        "AnimalCard",
        on_delete=models.CASCADE,
        related_name="photos",
    )

    image = models.ImageField(
        upload_to=get_animal_avatar_path,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.animal.name} photo"


def ensure_required_case(value: str) -> str:
    return value.capitalize()


def validate_not_use_underscore(value: str) -> str:
    if "_" in value:
        msg = _("The value should not contain underscores.")
        raise ValidationError(msg)
    return value


class AnimalCard(models.Model):
    """..."""

    name = models.CharField(
        max_length=100,
        validators=[
            ensure_required_case,
            validate_not_use_underscore,
        ],
    )

    age = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def last_photo(self) -> AnimalPhoto:
        return self.photos.last()

    def __str__(self) -> str:
        return f"{self.name}, {self.age} y.o."

    def save(self, *args, **kwargs) -> None:
        self.name = ensure_required_case(self.name)

        self.full_clean()

        super().save(*args, **kwargs)
