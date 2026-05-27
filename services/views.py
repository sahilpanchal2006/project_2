from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import ServiceCategory, Product
from .forms import QuoteForm


def service_list(request):
    """List all service categories."""
    categories = ServiceCategory.objects.all()
    context = {
        'services': categories,
    }
    return render(request, 'services/service_list.html', context)


from .models import Quote

def quote_form(request):
    """Handle quote request form: GET renders form, POST validates and saves."""
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you! Your quote request has been submitted successfully. '
                'We will get back to you within 24 hours.'
            )
            return redirect('quote_form')
    else:
        initial = {}
        material = request.GET.get('material')
        finish = request.GET.get('finish')
        
        # Check if the material is valid
        valid_materials = [m[0] for m in Quote.MATERIAL_CHOICES]
        if material in valid_materials:
            initial['material_choice'] = material
            
        # Check if the finish is valid
        valid_finishes = [f[0] for f in Quote.FINISH_TYPE_CHOICES]
        if finish in valid_finishes:
            initial['finish_type'] = finish
            
        form = QuoteForm(initial=initial)

    context = {
        'form': form,
    }
    return render(request, 'services/quote_form.html', context)


def product_list(request, category_slug=None):
    """List all products, optionally filtered by service category."""
    categories = ServiceCategory.objects.all()
    products = Product.objects.all()
    selected_category = None

    if category_slug:
        selected_category = get_object_or_404(ServiceCategory, slug=category_slug)
        products = products.filter(category=selected_category)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    }
    return render(request, 'services/product_list.html', context)

