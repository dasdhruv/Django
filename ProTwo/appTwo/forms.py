from django import forms
from .models import User

class RegisterNewUser(forms.ModelForm):
    # Add custom validations
    class Meta():
        model = User
        fields = '__all__'
