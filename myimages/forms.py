from django import forms
from app.models import Image


class ChangeImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['description', 'category']
