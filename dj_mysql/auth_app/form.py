
from django import forms

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(
    #     label="e-mail",
    #     strip=False,
    #     widget=forms.EmailInput(attrs={
    #         'autocomplate': 'new-email'
    #     })
    # )


    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplate': 'new-password'}),

    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplate': 'new-password'}),
        strip=False,

    )



    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")

    # class Meta(UserCreationForm.Meta):
    #     fiedls = UserCreationForm.Meta.fields + ("password1", "password2")