from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),  # List all products
    path('category/<slug:category_slug>/', views.CategoryDetailView.as_view(), name='category_detail'),  # Products by category
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),  # Product detail
    path('purchase/<slug:slug>/', views.PurchaseProductView.as_view(), name='process_purchase'),
    path('checkout/<slug:slug>/', views.CheckoutView.as_view(), name='checkout'),
    path('purchase-confirmation/', views.PurchaseConfirmationView.as_view(), name='purchase_confirmation'),

]
