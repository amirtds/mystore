from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.timezone import now

from .models import Product, Category, Customer, Purchase


class ProductListView(ListView):
    model = Product
    paginate_by = 10  # Adjust the number of items per page as needed
    template_name = 'store/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(available=True)  # Show only available products


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object, available=True)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


class PurchaseProductView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs['slug'], available=True)
        
        # Simulate a purchase by creating or retrieving a Customer entry and updating stock
        customer, created = Customer.objects.get_or_create(
            email=request.POST.get('email'),
            defaults={'name': request.POST.get('name')}
        )
        
        if product.stock > 0:
            Purchase.objects.create(
                customer=customer,
                product=product,
                purchase_date=now()
            )
            product.stock -= 1  # Decrement the product stock
            product.save()  # Save the product's new stock count
            messages.success(request, 'Thank you for your purchase!')
            
            # Redirect to a purchase confirmation page
            return redirect('purchase_confirmation')
        else:
            # If the product is out of stock, add an error message
            messages.error(request, 'This product is out of stock.')
            return redirect('product_detail', slug=product.slug)
    
class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, slug=kwargs['slug'], available=True)
        context = {'product': product}
        return render(request, 'store/checkout.html', context)

class PurchaseConfirmationView(View):
    template_name = 'store/purchase_confirmation.html'
    
    def get(self, request, *args, **kwargs):
        # Assuming you want to show a simple confirmation message
        return render(request, self.template_name)