from django_filters import rest_framework as filters
from django.db.models import Q

from .models import Book


class MultipleFilter(filters.Filter):

    def filter(self, qs, value):
        if not value:
            return qs
        query = Q()
        values = value.split(',')
        for v in values:
            query |= Q(writers__pk=v)
        return qs.filter(query)


class BookFilter(filters.FilterSet):
    writers = MultipleFilter(
        field_name='writers__pk',
        lookup_expr='in',
    )

    publisher = filters.CharFilter(
        field_name='publisher__pk',
        lookup_expr='exact',
    )

    class Meta:
        model = Book
        fields = ['writers', 'publisher']
