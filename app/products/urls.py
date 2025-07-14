from django.urls import path
from products.views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView
from .views import ActualPricesView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('items', ProductListView.as_view(), name='product-list'),
    path('items/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('get-actual-prices', ActualPricesView.as_view(), name='get-actual-prices'),
]
