from django import forms
from .models import User, Property

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'is_seller', 'password']

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['place', 'area', 'bedrooms', 'bathrooms', 'hospitals_nearby', 'colleges_nearby']