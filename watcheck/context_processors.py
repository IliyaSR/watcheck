from watcheck.common.models import Bag  # Import your Bag model


def watches_on_bag(request):
    count_watches_on_bag = Bag.objects.count()
    return {'count_watches_on_bag': count_watches_on_bag}
