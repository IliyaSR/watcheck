from django.contrib import admin

from watcheck.watch.models import Watch


# Register your models here.
@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'watch_code', 'price']
    filter = ['brand']


