from django import forms
from django.core.exceptions import ValidationError

# create form here

class BaseForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if not password == confirm_password:
            raise ValidationError(
                'confirm password not match'
            )


class UserForm(BaseForm):
    role = forms.CharField(widget=forms.HiddenInput(),initial='3')
    

class SellerForm(BaseForm):
    role = forms.CharField(widget=forms.HiddenInput(),initial='2')
    gstno = forms.CharField(max_length=100)
    
class LoginForm(forms.Form):
    phone = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())
