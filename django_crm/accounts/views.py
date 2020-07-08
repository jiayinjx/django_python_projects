from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import *


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):

    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers': customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, customer_pk):
    customer = Customer.objects.get(id = customer_pk)
    customer_orders = customer.order_set.all()
    customer_orders_count = customer_orders.count()

    filter = OrderFilter(request.GET, queryset=customer_orders)
    customer_orders = filter.qs

    context = {'customer': customer, 'customer_orders':customer_orders, 'customer_orders_count': customer_orders_count, 'filter': filter}
    return render(request, 'accounts/customer.html', context)

def createOrder(request, customer_pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id = customer_pk)

    # order_form = OrderForm(initial={'customer':customer})
    order_form_set = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method  == 'POST':
        # print('Printing POST: ', request.POST)
        # order_form = OrderForm(request.POST)
        order_form_set = OrderFormSet(request.POST, instance=customer)
        if order_form_set.is_valid():
            order_form_set.save()
            return redirect('/')

    context = {'order_form': order_form_set}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, order_pk):
    order = Order.objects.get(id=order_pk)
    order_form = OrderForm(instance=order)

    if request.method  == 'POST':
        # print('Printing POST: ', request.POST)
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order_form.save()
            return redirect('/')

    context = {'order_form': order_form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, order_pk):
    order = Order.objects.get(id=order_pk)

    if request.method  == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
