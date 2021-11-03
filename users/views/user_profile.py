from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import ProfileForm, AddressForm
from users.models import Profile, Address


@login_required()
def profile_view(request):
    user_pk = request.user
    a = Address.objects.filter(user=user_pk).first()
    p = Profile.objects.filter(user=user_pk).first()
    if request.method == 'GET':
        form_a = AddressForm(user_pk, instance=a)
        form_p = ProfileForm(user_pk, instance=p)
    else:
        form_a = AddressForm(user_pk, request.POST, instance=a)
        form_p = ProfileForm(user_pk, request.POST, files=request.FILES, instance=p)
        form_a.save()
        form_p.save()

        return redirect('/users/login_view/')
    return render(request, 'users/profile.html', {
        'form_a': form_a,
        'form_p': form_p
    })
