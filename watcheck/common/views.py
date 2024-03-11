from django.shortcuts import render, redirect

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