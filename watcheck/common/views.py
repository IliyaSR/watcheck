from itertools import chain

from django.shortcuts import render, redirect

from watcheck.accounts.models import Account
from watcheck.common.forms import OrderForm
from watcheck.common.models import Bag
from watcheck.watch.models import Watch


# Create your views here.
def home(request):
    return render(request, template_name='common/home.html')


def about(request):
    return render(request, template_name='common/about-us.html')


def stores(request):
    return render(request, template_name='common/stores.html')


def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        watches = Watch.objects.filter(brand__icontains=searched)
        if watches:
            context = {
                'watches': watches
            }
            return render(request, 'watch/shop.html', context=context)
        else:
            return render(request, 'common/search.html')


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


def checkout(request, pk):
    bag_elements = Bag.objects.all()
    watches_codes = [current_element.watch_code for current_element in bag_elements]
    product_price = 0
    for current_element in bag_elements:
        product_price += current_element.price

    sum_with_delivery = product_price + 8

    if request.method == "POST":
        form = OrderForm(request.POST)
        user = Account.objects.get(pk=pk)
        watches = Watch.objects.filter(watch_code__in=watches_codes)

        if form.is_valid():
            order = form.save(commit=False)
            order.current_profile = user
            for watch in watches:
                order.brand_watch = watch
            bag_elements.delete()
            order.save()
            return redirect('home')
    else:
        form = OrderForm()

    context = {
        'bag_elements': bag_elements,
        'product_price': product_price,
        'sum_with_delivery': sum_with_delivery,
        'form': form
    }

    return render(request, template_name='common/checkout.html', context=context)
