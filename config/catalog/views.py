from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Каталог Electrostore',
        'object_list': Product.objects.all()
    }


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


def product(request, product_id):

    object = Product.objects.get(pk=product_id).__dict__
    context = {
        'object': object
    }
    return render(request, 'catalog/product.html', context)