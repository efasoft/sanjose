from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'edad', 'fecha', 'email']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
