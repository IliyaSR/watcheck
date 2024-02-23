from django.shortcuts import render


# Create your views here.
def shop(request):
    return render(request, template_name='watch/shop.html')


def watch_details(request, pk):
    return render(request, template_name='watch/watch-details.html')