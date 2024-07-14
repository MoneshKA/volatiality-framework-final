# from django import forms
# from .models import PluginAnalysis

# class PluginUploadForm(forms.ModelForm):
#     class Meta:
#         model = PluginAnalysis
#         fields = ['plugin_folder']
#         widgets = {
#             'plugin_folder': forms.ClearableFileInput(attrs={'multiple': False}),
#         }
# from django import forms
# from .models import PluginAnalysis

# class PluginUploadForm(forms.ModelForm):
#     class Meta:
#         model = PluginAnalysis
#         fields = ['plugin_name', 'plugin_folder']
#         widgets = {
#             'plugin_folder': forms.ClearableFileInput(attrs={'multiple': False}),
#         }
from django import forms
from .models import PluginAnalysis, MemoryDump
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class PluginUploadForm(forms.ModelForm):
    class Meta:
        model = PluginAnalysis
        fields = ['plugin_name', 'plugin_folder']

class MemoryDumpUploadForm(forms.ModelForm):
    class Meta:
        model = MemoryDump
        fields = ['file']


# plugin/forms.py

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

