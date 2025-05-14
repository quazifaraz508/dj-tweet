from django.shortcuts import render

# Create your views here.
from .models import Product

def home(request):
    products = Product.objects.all()
    is_owner = request.user.is_superuser  # This will check if logged-in user is the owner
    return render(request, 'home.html', {'products': products, 'is_owner': is_owner})
