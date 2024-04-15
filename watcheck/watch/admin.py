from django.contrib import admin

from watcheck.watch.models import Watch, Review


# Register your models here.
@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'watch_code', 'price', 'case_diameter']
    list_filter = ['brand', 'price', 'case_diameter']
    ordering = ['brand']
    search_fields = ['brand']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'rated_watch', 'person_review']