from django import forms

from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    #TODO email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['birthday', 'avatar',]
