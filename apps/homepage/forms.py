from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

from django.forms.widgets import PasswordInput, TextInput, EmailInput
from django.core.exceptions import ValidationError

User = get_user_model()

class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=200, 
        help_text='requerido', 
        widget=EmailInput(attrs={'class':'form-control', 'placeholder':'correo electrónico'})
    )
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

        """
        widgets = {

            "username":TextInput(attrs={'class':'form-control', 'placeholder':'usuario'}),

        }
        """

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Contraseñas no coinciden")
            
        return password2

    """
    def clean_email(self):
        email = self.cleaned_data['email']
        if (("@fpuna.edu.py" not in email) and ("@fiuna.edu.py" not in email)):
            raise ValidationError("Debe ser un correo académico (@fpuna.edu.py o @fiuna.edu.py)")

        if (User.objects.filter(email=email)):
        	raise ValidationError("Ya existe una cuenta asociada a ese correo")


        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return email
    """



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({'class': 'form-control', 'placeholder':'Nombres'})
        self.fields["last_name"].widget.attrs.update({'class': 'form-control', 'placeholder':'Apellidos'})

        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder':'Contraseña'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder':'Confirmar contraseña'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user