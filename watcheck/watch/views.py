from itertools import chain

from django.db.models import Q
from django.shortcuts import render

from watcheck.watch.models import Watch


# Create your views here.
def shop(request):
    watches = Watch.objects.all()
    context = {
        'watches': watches
    }

    return render(request, template_name='watch/shop.html', context=context)


def filter_watches(request):
    brand = request.GET.getlist('brand')
    price = request.GET.getlist('price')
    watches = Watch.objects.all()

    if len(price) == 1:
        current_price = [int(watch_price) for watch_price in price[0].split(', ')]
    else:
        current_price = []
        for index in range(len(price)):
            current_price.append([int(watch_price) for watch_price in price[index].split(', ')])

    if brand:
        watches = watches.filter(brand__in=brand)
    if price:
        if len(price) == 1:
            watches = watches.filter(price__range=current_price)
        else:
            result = []
            for price in current_price:
                result.append(watches.filter(price__range=price))

            watches = list(chain(*result))

    return render(request, template_name='watch/shop.html', context={"watches": watches})


def watch_details(request, pk):
    current_watch = Watch.objects.get(pk=pk)
    context = {
        'current_watch': current_watch
    }

    return render(request, template_name='watch/watch-details.html', context=context)
