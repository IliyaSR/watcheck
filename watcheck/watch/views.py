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
    watches = Watch.objects.all()

    if brand:
        watches = watches.filter(brand__in=brand)

    return render(request, template_name='watch/shop.html', context={"watches": watches})


def watch_details(request, pk):
    current_watch = Watch.objects.get(pk=pk)
    context = {
        'current_watch': current_watch
    }

    return render(request, template_name='watch/watch-details.html', context=context)
