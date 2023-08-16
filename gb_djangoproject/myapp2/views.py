from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from myapp2.models import Client, Order, Product
from datetime import datetime, timedelta
import logging
from .forms import ProductForm

logger = logging.getLogger(__name__)


def client_products(request, client_id, days):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__gte=datetime.now() - timedelta(days=days))
    products = []
    for order in orders:
        products.extend([i.name for i in order.products.all()])

    context = {'client': client, 'days': days, 'products': set(products)}
    return render(request, 'myapp2/client_products.html', context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']

            product.name = name
            product.description = description
            product.price = price
            product.count = count
            product.image = image
            product.save()

            message = 'Продукт сохранён'
            logger.info(f'Получили {str(product)}')
        else:
            message = 'Что-то пошло не так...'
    else:
        message = 'Заполните форму'
        form = ProductForm()

    return render(request, 'myapp2/edit_product.html', {'form': form, 'message': message})