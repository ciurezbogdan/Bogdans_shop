from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware
from users.middlewares.activation import ValidateTokenMiddleware
from users.models import Activation
from django.utils import timezone
from utils.constants import ACTIVATION_DICT
from users.emails import send_activation_email
import secrets
from users.forms import UserActivation
from django.contrib.auth import authenticate, login


@decorator_from_middleware(ValidateTokenMiddleware)
def activation_view(request, token):
    activation = Activation.objects.get(token=token)  # activation.user

    if request.method == 'GET':
        form = UserActivation(activation.user)
    else:
        form = UserActivation(activation.user, request.POST)

    if form.is_valid():
        form.save()

        # Log In user.
        email = activation.user.email
        password = form.cleaned_data.get('password')
        authenticated_user = authenticate(request, username=email, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)

        return redirect('/')

    return render(request, 'users/activation/activate.html', {
        'token': token,
        'form': form,
    })


@decorator_from_middleware(ValidateTokenMiddleware)
def reset_token(request, token):
    if request.method == 'GET':
        return render(request, 'users/activation/reset_token.html', {
            'token': token
        })
    # reset token
    activation = Activation.objects.get(token=token)
    activation.token = secrets.token_hex(32)
    activation.expires_at = timezone.now() + timezone.timedelta(**ACTIVATION_DICT)
    activation.save()

    send_activation_email(activation)

    return redirect('/')  # after request pe post always redirect otherwise refresh or F5 generate new token
