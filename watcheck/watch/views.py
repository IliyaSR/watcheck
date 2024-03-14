from itertools import chain

from django.db.models import Q
from django.shortcuts import render, redirect

from watcheck.watch.forms import ReviewForm
from watcheck.watch.models import Watch, Review


def string_to_integer_func(element):
    if len(element) == 1:
        current_elements = [int(current_element) for current_element in element[0].split(',')]
    else:
        current_elements = []
        for index in range(len(element)):
            current_elements.append([int(current_element) for current_element in element[index].split(',')])

    return current_elements


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
    case_diameter = request.GET.getlist('case_diameter')
    watches = Watch.objects.all()

    current_price = string_to_integer_func(price)
    current_case_diameters = string_to_integer_func(case_diameter)

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

    if case_diameter:
        if len(case_diameter) == 1:
            watches = watches.filter(case_diameter__range=current_case_diameters)
        else:
            print(case_diameter)
            result = []
            for case_diameter in current_case_diameters:
                result.append(watches.filter(case_diameter__range=case_diameter))

            watches = list(chain(*result))

    return render(request, template_name='watch/shop.html', context={"watches": watches})


def watch_details(request, pk):
    current_watch = Watch.objects.get(pk=pk)
    reviews = Review.objects.filter(rated_watch__pk=pk)
    review_form = ReviewForm()
    numbers_stars = range(1, 6)
    average_rating = 0
    if reviews:
        sum_of_ratings = 0
        for review in reviews:
            sum_of_ratings += review.rating

        average_rating = sum_of_ratings / len(reviews)

    context = {
        'current_watch': current_watch,
        'reviews': reviews,
        'numbers_stars': numbers_stars,
        'average_rating': average_rating,
        'review_form': review_form
    }

    return render(request, template_name='watch/watch-details.html', context=context)


def add_review(request, watch_id):
    rated = request.GET.getlist('selected')
    print(rated)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        watch = Watch.objects.get(id=watch_id)

        if form.is_valid():
            review = form.save(commit=False)
            review.rated_watch = watch
            review.person_review = request.user
            review.save()

            return redirect(request.META['HTTP_REFERER'] + f'#{watch_id}')


