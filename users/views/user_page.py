from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404
from users.models import AuthUser
from products.models import Products
from django.urls import reverse
from django.http import HttpResponseRedirect


@login_required()
def user_page_view(request, user_id=None):

    try:
        user = AuthUser.objects.get(pk=user_id)
    except AuthUser.DoesNotExist:
        raise Http404('Store with ID %d does not exist.' % user_id)

    return render(request, 'users/user_page.html', {
        'user': user,
        'products': user.products.all()
    })


@ login_required()
def login_view(request):
    return HttpResponseRedirect(
               reverse('users:user_page',
                       args=[request.user.id]))

#
# def user_products(request, user_id):
#     if request.user.is_authenticated:
#         product = Products.objects.filter(user=user_id).all()
#     return render(request, 'users/user_products.html', {
#         'user_products': product
#     })
