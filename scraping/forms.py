from django import forms

from .models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset = City.objects.all(),
        to_field_name="slug",
        required = False,
        label = "City",
        widget = forms.Select(
            attrs ={"class": "form-control"}
        )
    )
    language = forms.ModelChoiceField(
        queryset = Language.objects.all(),
        to_field_name="slug",
        label= 'Language',
        required = False,
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )