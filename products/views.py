from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from django.core.paginator import Paginator
from products.forms.filter import SearchAndFilter
from products.forms.add_item import ProductForm
from products.forms.product_details import ProductDetailsForm
from django.views.generic import ListView
from .models import Category, Products, ProductCategories
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


# Create your views here.


class ProductView(ListView):
    model = Products
    context_object_name = 'products_list'
    template_name = 'products/products_list.html'
    paginate_by = 3


def list_view(request):
    form = SearchAndFilter(request.GET)
    products_list = form.get_filtered_products()  # Products.objects.all()
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/products_list.html', {
        'page_obj': page_obj,
        'form': form,
    })


def view_all_products(request):
    # if request.user.is_authenticated:
    product = Products.objects.all()

    return render(request, 'products/test2.html', {
        'product_list1': product
    })


def category_list(request, category):
    category_obj = Category.objects.get(name=category)
    category_id = category_obj.id
    products_list = Products.objects.filter(category=category_id)
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/category_list.html', {
        'page_obj': page_obj,
        'category': category_obj
    })


@login_required()
def add_product_view(request):
    user_pk = request.user
    if request.method == 'GET':
        form = ProductForm(user_pk)
    else:
        form = ProductForm(user_pk, request.POST, files=request.FILES)
        if form.is_valid():
            item = form.save()
            categories_pick = form.cleaned_data.get('category')
            for category in categories_pick:
                item.category.add(category)
            return redirect(reverse('users:login_view'))
    return render(request, 'products/add_product.html', {
        'form': form
    })


@login_required()
def product_details(request, product_id):
    item = Products.objects.get(id=product_id)
    if request.method == 'GET':
        form = ProductDetailsForm(instance=item)
    else:
        form = ProductDetailsForm(request.POST, instance=item)
        if form.has_changed() and form.is_valid():
            form.save()
        return redirect('/users/login_view/')
    return render(request, 'products/details.html', {
        'form': form
    })
