from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html, validate_password
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

AuthUser = get_user_model()


# class RegisterForm(UserCreationForm):
#     pass

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = AuthUser
#         fields = ['first_name', 'last_name', 'email', 'password']


# class RegisterForm(forms.Form):
#     # fileds definition
#     first_name = forms.CharField(label='First Name', max_length=255, required=True)
#     last_name = forms.CharField(label='Last Name', max_length=255, required=True)
#     email = forms.EmailField(label='Email', max_length=255, required=True)
#
#     # email validation option 1
#     # def clean_email(self):
#     #     email = self.cleaned_data
#     #     user = AuthUser.objects.filter(email=email).first()
#     #     if user:
#     #         raise forms.ValidationError('Not a valid email !!!')
#     #     return email
#
#     # email validation option 2
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         print(email)
#         try:
#             AuthUser.objects.get(email=email)
#         except AuthUser.DoesNotExist:
#             return email
#         else:
#             raise forms.ValidationError('Not a valid email !!!')
#
#     def save(self):
#         first_name = self.cleaned_data.get('first_name')
#         last_name = self.cleaned_data.get('last_name')
#         email = self.cleaned_data.get('email')
#
#         user = AuthUser.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password='Python123'
#         )
#         return user

class RegisterForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        email = self.cleaned_data['email']
        self.instance.username = email

        return super().save(commit)


class UserActivation(forms.Form):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        help_text=password_validators_help_text_html(),
    )

    password_confirmation = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=True,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password, self.user)

        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password_confirmation != password:
            raise forms.ValidationError('Password confirmation mismatch.')

        return password_confirmation

    def save(self):
        self.user.set_password(self.cleaned_data.get('password'))
        self.user.is_active = True
        self.user.save()


class UserCreationForm(BaseUserCreationForm):
    password1 = None
    password2 = None

    def clean_password2(self):
        pass

    def save(self, commit=True):
        user = super(BaseUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
