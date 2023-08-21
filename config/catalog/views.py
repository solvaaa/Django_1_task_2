from django.shortcuts import render
from catalog.models import Product


# Create your views here.
def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


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