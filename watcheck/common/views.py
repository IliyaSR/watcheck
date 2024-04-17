from itertools import chain

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect

from watcheck.accounts.forms import AddressForm
from watcheck.accounts.models import Account, Address
from watcheck.common.forms import OrderForm
from watcheck.common.models import Bag, Order
from watcheck.watch.models import Watch


def staff_required(user):
    return user.is_superuser or user.is_staff


# Create your views here.
def home(request):
    is_open_home = 'the page is open'
    return render(request, template_name='common/home.html', context={"is_open_home": is_open_home})


def about(request):
    is_open_about = 'the page is open'
    return render(request, template_name='common/about-us.html', context={"is_open_about": is_open_about})


def stores(request):
    is_open_stores = 'the page is open'
    return render(request, template_name='common/stores.html', context={"is_open_stores": is_open_stores})


def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        watches = Watch.objects.filter(Q(brand__icontains=searched) | Q(watch_code__icontains=searched))
        if watches:
            context = {
                'watches': watches
            }
            return render(request, 'watch/shop.html', context=context)
        return render(request, 'common/search.html')


@login_required(login_url='sign_in')
def bag_view(request):
    bag_elements = Bag.objects.all()
    product_price = 0
    for current_element in bag_elements:
        product_price += current_element.price

    sum_with_delivery = product_price + 8
    context = {
        'bag_elements': bag_elements,
        'product_price': product_price,
        'sum_with_delivery': sum_with_delivery
    }
    return render(request, template_name='common/bag.html', context=context)


def add_to_bag_view(request, pk):
    current_watch = Watch.objects.get(pk=pk)
    bag_element = Bag(watch_image=current_watch.main_image, brand_watch=current_watch.brand,
                      model_watch=current_watch.model,
                      price=current_watch.price, watch_code=current_watch.watch_code)
    bag_element.save()
    return redirect('watch_details', pk)


def remove_item_from_bag(request, pk):
    current_element = Bag.objects.get(pk=pk)
    current_element.delete()

    return redirect('bag')


@login_required(login_url='sign_in')
def checkout(request, pk):
    bag_elements = Bag.objects.all()
    watches_codes = [current_element.watch_code for current_element in bag_elements]
    product_price = 0
    for current_element in bag_elements:
        product_price += current_element.price

    sum_with_delivery = product_price + 8
    user = Account.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        watches = Watch.objects.filter(watch_code__in=watches_codes)
        if 'ordering' in request.POST:
            if form.is_valid():
                order = form.save(commit=False)
                order.current_profile = user
                order.save()
                order.current_watch.set(watches)
                bag_elements.delete()
                return redirect('home')
        if 'clean' in request.POST:
            form = OrderForm()
    else:
        if user.address_set.all():
            address = Address.objects.get(current_profile_id=pk)
            form = OrderForm(instance=address)
        else:
            form = OrderForm()

    context = {
        'bag_elements': bag_elements,
        'product_price': product_price,
        'sum_with_delivery': sum_with_delivery,
        'form': form
    }

    return render(request, template_name='common/checkout.html', context=context)


def guarantee(request):
    return render(request, template_name='common/guarantee and warranty.html')


@login_required(login_url='sign_in')
@user_passes_test(staff_required)
def check_all_orders(request):
    all_orders = Order.objects.all()

    context = {
        'all_orders': all_orders,
    }

    return render(request, template_name='common/all_orders.html', context=context)


def contact_us(request):
    return render(request, template_name='common/contact-us.html')


def payment_options(request):
    return render(request, template_name='common/payment-options.html')


def shipping_policy(request):
    return render(request, template_name='common/shipping-policy.html')


def faq(request):
    return render(request, template_name='common/faq.html')
