from django.urls import reverse_lazy
from catalog.models import Product, BlogPost
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from random import randint

# Create your views here.


def get_slug(title):
    slug = "-".join(title.split())
    slug += '-'
    slug += str(randint(1, 10))
    return slug


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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.number_of_views += 1
        object.save()
        return object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.slug = get_slug(new_post.title)
        new_post.save()
        return super().form_valid(form)



class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('catalog:home')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:home')