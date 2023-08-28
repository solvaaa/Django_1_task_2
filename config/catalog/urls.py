from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductListView, ProductDetailView


app_name = CatalogConfig.name


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    #path('product/<int:product_id>/', product, name='product')

]