
from django import forms
from .models import GeneratedImages

class ImagesForm(forms.ModelForm):
    class Meta:
        model = GeneratedImages
        fields = ['img']
