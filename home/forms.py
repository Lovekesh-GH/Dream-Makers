from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import fields, widgets

class LoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'col-12','style':'border-radius: .5vw;height: 2.5vw;margin-bottom: 1vw; margin-left:.7vw; border-color: rgb(200, 202, 204);','placeholder':'Enter username'
        })
        self.fields['password'].widget.attrs.update({
            'class':'col-12','style':'border-radius: .5vw;height: 2.5vw;margin-bottom: 1.6vw; margin-left:.7vw; border-color: rgb(200, 202, 204);','placeholder':'Password'
        })

    class Meta:
        model = User
        fields = '__all__'


class RegistrationForm(UserCreationForm):

    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'col-12'}))
    password2 = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput(attrs={'class':'col-12'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':widgets.TextInput(attrs={'class':'col-12'}),'first_name':widgets.TextInput(attrs={'class':'col-5'}),'last_name':widgets.TextInput(attrs={'class':'col-5'}),'email':widgets.EmailInput(attrs={'required':True,'class':'col-12'})}