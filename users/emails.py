from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import reverse
from django.template.loader import get_template
from utils.constants import ACTIVATION_TIME


def send_register_email(user):

    send_mail(
        subject='Bogdan"s shop registration mail',
        message=f'Hello {user.first_name} {user.last_name} \n Welcome to our Antique Shop',
        from_email='ciurezbogdan81@gmail.com',  # can be removed, DEFAULT_FROM_EMAIL is present in settings.py
        recipient_list=[user.email]
    )


def send_activation_email(activation):
    user = activation.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'activation_url': f"http://localhost:8000{reverse('users:activation:activate', args=(activation.token,))}",
        'activation_value': ACTIVATION_TIME['value'],
        'activation_unit': ACTIVATION_TIME['units'],
    }

    template = get_template('users/emails/activation.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='Your account have been created',
        body=content,
        from_email='ciurezbogdan81@gmail.com',  # can be removed, DEFAULT_FROM_EMAIL is present in settings.py
        to=[user.email]
    )

    mail.content_subtype = 'html'
    mail.send()
