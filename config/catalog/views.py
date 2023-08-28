from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Каталог Electrostore',
    }


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


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
