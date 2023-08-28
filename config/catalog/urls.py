from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsView, ProductListView, ProductDetailView
from catalog.views import BlogPostListView


app_name = CatalogConfig.name


urlpatterns = [
    path('', BlogPostListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

]