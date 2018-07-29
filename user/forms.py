import re

from django import forms
from django.utils.translation import gettext_lazy as _

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(min_length=6, max_length=32,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data['username']
        pwd = self.cleaned_data['password']
        self.valid_username(username)
        self.valid_password(pwd)
        return cleaned_data

    def valid_username(self, username):
        try:
            self.user = User.objects.filter(username=username)[0]
        except IndexError:
            raise forms.ValidationError(_('该用户不存在'))

    def valid_password(self, pwd):
        if not self.user.valid_password(pwd):
            raise forms.ValidationError(_('密码错误'))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=16,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=6, max_length=32,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(min_length=6, max_length=32,
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data['username']
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        self.valid_username(username)
        self.valid_password(pwd1, pwd2)
        return cleaned_data

    def valid_username(self, username):
        if re.findall('[^0-9a-zA-Z_]', username):
            raise forms.ValidationError(_('用户名只允许使用数字字母或下划线'))
        if User.objects.filter(username=username):
            raise forms.ValidationError(_('用户名%(username)s已经被注册了'), params={'username': username})

    def valid_password(self, pwd1, pwd2):
        if re.findall('[^0-9a-zA-Z_]', pwd1):
            raise forms.ValidationError(_('密码只允许使用数字字母或下划线'))
        if pwd1 != pwd2:
            raise forms.ValidationError(_('两次密码输入不一致'))

