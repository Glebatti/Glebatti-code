from django.contrib import admin, messages
from .models import Movie, Director, Actor
from django.db.models import QuerySet

# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['budget']
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status', 'director']
    list_editable = ['rating', 'currency', 'budget', 'director']
    filter_horizontal = ['actors']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__istartswith', 'rating']

    # admin.site.register(Movie, MovieAdmin)
    @admin.display(ordering='rating', description='rating_status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Зачем это смотреть?!'
        if mov.rating < 70:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей',
            # messages.ERROR
        )
