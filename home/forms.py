
from django import forms
from .models import ImageModel

class ImgForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']
