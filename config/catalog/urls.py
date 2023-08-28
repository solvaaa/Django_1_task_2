from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView
from catalog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView
from catalog.views import BlogPostUpdateView, BlogPostDeleteView


app_name = CatalogConfig.name


urlpatterns = [
    path('', BlogPostListView.as_view(), name='home'),
    path('blog/<slug>/', BlogPostDetailView.as_view(), name='blogpost'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('edit/<slug>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('delete/<slug>/', BlogPostDeleteView.as_view(), name='delete_blogpost'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]