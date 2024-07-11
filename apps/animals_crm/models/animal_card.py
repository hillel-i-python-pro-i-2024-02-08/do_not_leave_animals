# noinspection PyPackageRequirements
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .animal_photo import AnimalPhoto
from .animal_comment import AnimalComment


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

    def last_comment(self) -> AnimalComment:
        return self.comments.last()

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs) -> None:
        try:
            self.name = validate_not_use_underscore(self.name)
            self.name = ensure_required_case(self.name)

            self.full_clean()

            super().save(*args, **kwargs)
        except Exception as e:
            print(e)

    description = models.TextField(max_length=1000, null=True, blank=True)
