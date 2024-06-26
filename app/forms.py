from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = UserCreationForm.Meta.fields
        fields = ('username', 'first_name', 'last_name', 'email')

    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    #
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email')
    #
    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']

