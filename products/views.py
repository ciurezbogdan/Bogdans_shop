from django.shortcuts import render, HttpResponse, Http404
from products.models import Products
from django.core.paginator import Paginator

from django.views.generic import ListView
from .models import Category, Products


# Create your views here.

class ProductView(ListView):
    model = Products
    context_object_name = 'products_list'
    template_name = 'products/products_list.html'
    paginate_by = 3


def list_view(request):
    # form = SearchAndFilterPizza(request.GET)
    products_list = Products.objects.all()           # form.get_filtered_pizza()
    paginator = Paginator(products_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/products_list.html', {
        'page_obj': page_obj,
        # 'form': form,
    })


def view_all_products(request):
    # if request.user.is_authenticated:
    product = Products.objects.all()

    return render(request, 'products/test2.html', {
        'product_list1': product
    })


def add_product_view(request):
    return render(request, 'products/add_product.html', {})


def product_details(request, product_id):
    return HttpResponse('Product id is %s' % product_id)

# class CategoryList(ListView):
#     model = Category
#     template_name = 'templates/homepage.html'
#     context_object_name = 'category_list'
