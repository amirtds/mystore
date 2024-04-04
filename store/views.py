from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.timezone import now

# Import OpenTelemetry's trace module for creating custom spans
from opentelemetry import trace
# Import AppSignal's set_root_name for customizing the trace name
from appsignal import set_root_name, set_category

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
        # Initialize the tracer for the current application context
        tracer = trace.get_tracer(__name__)
        
        # Define the overall span for the view
        with tracer.start_as_current_span("PurchaseProductView") as span:
            # Set AppSignal trace details for better organization
            set_root_name("POST /store/purchase/<slug>")
            set_category("process.purchase")

            # Attempt to retrieve the product and handle cases where it's not found
            product = get_object_or_404(Product, slug=kwargs['slug'], available=True)
            
            # Create a nested span for the customer retrieval/creation process
            with tracer.start_as_current_span("Retrieve or Create Customer"):
                customer, created = Customer.objects.get_or_create(
                    email=request.POST.get('email'),
                    defaults={'name': request.POST.get('name')}
                )
            
            # Create a nested span for the purchase creation process
            with tracer.start_as_current_span("Create Purchase Record"):
                if product.stock > 0:
                    Purchase.objects.create(
                        customer=customer,
                        product=product,
                        purchase_date=now()
                    )
                    product.stock -= 1  # Decrement the product's stock
                    product.save()  # Save the updated product information
                    messages.success(request, 'Thank you for your purchase!')
                    
                    # Redirect to a confirmation page
                    return redirect('purchase_confirmation')
                else:
                    # Add an error message if the product is out of stock and redirect
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