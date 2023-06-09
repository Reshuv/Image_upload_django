from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    """ Form for the image model """
    class Meta:
        model = Image

        fields = ['name', 'image']