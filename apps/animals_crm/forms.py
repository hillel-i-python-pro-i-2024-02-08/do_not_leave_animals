from django import forms
from .models import AnimalCard, AnimalPhoto, AnimalComment
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from string import punctuation, digits


class AnimalCardForm(forms.ModelForm):
    class Meta:
        model = AnimalCard
        fields = ["name", "age", "description"]
        labels = {
            "name": _("Name of beauty"),
            "age": _("Age in y.o."),
            "description": _("Some description of beauty"),
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        name.strip().title()
        for char in name:
            if char in punctuation or char in digits or char in " \t\n":
                raise ValidationError("Name must not have digits or punctuation characters")
        return name

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 0 or age > 50:
            raise ValidationError("This is some incorrect age bro :)")
        return age


AnimalPhotoFormSet = forms.inlineformset_factory(
    parent_model=AnimalCard,
    model=AnimalPhoto,
    fields=["image"],
    labels={"image": "Photo or video"},
    extra=1,
    max_num=10,
    validate_max=True,
)

AnimalCommentFormSet = forms.inlineformset_factory(
    parent_model=AnimalCard,
    model=AnimalComment,
    fields=["comment_text"],
    labels={"comment_text": "Record about animal status"},
    extra=1,
)
