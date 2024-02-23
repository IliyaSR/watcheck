from django.shortcuts import render

from watcheck.watch.models import Watch


# Create your views here.
def shop(request):
    watches = Watch.objects.all()
    context = {
        'watches': watches
    }

    return render(request, template_name='watch/shop.html', context=context)


def watch_details(request, pk):
    return render(request, template_name='watch/watch-details.html')
