from django import forms
from app.models import Image


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description', 'category']
