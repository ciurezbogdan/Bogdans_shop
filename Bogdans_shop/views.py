from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {
        'brand': "Bogdan's Shop"
    })


def contact_view(request):
    return render(request, 'contact.html')