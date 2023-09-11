from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from catalog.models import Product, BlogPost, Version
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        versions = {}
        for object in context['object_list']:
            pk = object.pk
            versions[pk] = Version.objects.filter(is_active=True, product=pk)
        context['versions'] = versions
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = context['object'].pk
        context['versions'] = Version.objects.filter(is_active=True, product=pk)
        return context


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
    extra_context = {
        'button_name': "Создать"
    }
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview', 'is_published')
    extra_context = {
        'button_name': "Редактировать"
    }

    def get_success_url(self):
        return reverse("catalog:blogpost", args=[self.kwargs.get('slug')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:home')


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product
    extra_context = {
        'form_name': 'Добавление',
        'button_name': 'Добавить'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = self.request.user
            new_post.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product
    extra_context = {
        'form_name': 'Редактирование',
        'button_name': 'Редактировать'
    }
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "users:login"
    redirect_field_name = "redirect_to"
    model = Product
    success_url = reverse_lazy('catalog:catalog')