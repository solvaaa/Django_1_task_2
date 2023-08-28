from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Каталог Electrostore',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["object_list"] = Product.objects.all()
        return context_data


'''def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')'''


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"
    extra_context = {
        'title': "Контакты Electrostore",
    }

    def post(self, request):
        name = self.request.POST.get('name')
        email = self.request.POST.get('email')
        message = self.request.POST.get('message')
        context = {}
        print(f'You have new message from {name}({email}): {message}')
        return super(TemplateView, self).render_to_response(context)

def product(request, product_id):

    object = Product.objects.get(pk=product_id).__dict__
    context = {
        'object': object
    }
    return render(request, 'catalog/product.html', context)