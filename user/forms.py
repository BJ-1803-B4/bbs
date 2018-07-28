import re

from django import forms

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    remeber_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        remeber_me = self.cleaned_data['remeber_me']
        if not self.valid_user(username, password):
            raise forms.ValidationError('')
        return cleaned_data

    # 用户名只可以是数字字母和下划线的组合，且用户名密码必须匹配
    def valid_user(self, username, password):
        if re.findall('[^0-9a-zA-Z_]', username):
            return False
        else:
            user = User.objects.filter(username=username)
            return User.objects.valid_password(password, user.password)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=16, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(min_length=6, max_length=32,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data['username']
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        if not self.valid_username(username):
            raise forms.ValidationError('')
        if not self.valid_password(pwd1, pwd2):
            raise forms.ValidationError('')
        return cleaned_data

    # 用户名只可以是数字字母和下划线的组合
    def valid_username(self, username):
        if re.findall('[^0-9a-zA-Z_]', username):
            return False
        return False if not User.objects.filter(username=username) else True

    # 两次密码必须一致，且只能是数字字母和下划线的组合
    def valid_password(self, pwd1, pwd2):
        if re.findall('[^0-9a-zA-Z_]', pwd1):
            return False
        return False if not pwd1 == pwd2 else True
