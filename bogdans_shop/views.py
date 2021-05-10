from django.http import HttpResponse
from django.shortcuts import render
from products.models import Category


def homepage(request):
    category_list = Category.objects.all()
    return render(request, 'homepage.html', {
        'brand': "Bogdan's Shop",
        'categories': category_list
    })


def contact_view(request):
    return render(request, 'contact.html')