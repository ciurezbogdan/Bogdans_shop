from django import forms
from django.contrib.auth import get_user_model

AuthUser = get_user_model()


class RegisterForm(forms.Form):
    # fileds definition
    first_name = forms.CharField(label='First Name', max_length=255, required=True)
    last_name = forms.CharField(label='Last Name', max_length=255, required=True)
    email = forms.EmailField(label='Email', max_length=255, required=True)

    # email validation option 1
    # def clean_email(self):
    #     email = self.cleaned_data
    #     user = AuthUser.objects.filter(email=email).first()
    #     if user:
    #         raise forms.ValidationError('Not a valid email !!!')
    #     return email

    # email validation option 2
    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        try:
            AuthUser.objects.get(email=email)
        except AuthUser.DoesNotExist:
            return email
        else:
            raise forms.ValidationError('Not a valid email !!!')

    def save(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')

        user = AuthUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password='Python123'
        )
        return user
