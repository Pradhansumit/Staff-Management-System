from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = models.CustomUserModel
        fields = ['name', 'email', 'phone_number',
                  'user_status',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if self.cleaned_data['user_status'] == 'staff':
            user.is_staff = True

        if self.cleaned_data['user_status'] == 'admin':
            user.is_staff = True
            user.is_superuser = True

        if commit:
            user.save()
        return user
