from django import forms
from django.forms import ModelForm, fields
from .models import Image

#create a model form here
class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

        



