from django.urls import reverse_lazy
from catalog.models import Product, BlogPost
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.


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


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:home')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:home')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:home')