from collections import OrderedDict

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Publisher, Writer, Book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['pk', 'name', 'phone', 'address']


class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['pk', 'first_name', 'last_name', 'sure_name']


class WriterField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(WriterField, self).to_representation(value)
        try:
            item = Writer.objects.get(pk=pk)
            serializer = WriterSerializer(item)
            return serializer.data
        except Writer.DoesNotExist:
            return None

    def get_queryset(self):
        return Writer.objects.all()

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])


class PublisherField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        pk = super(PublisherField, self).to_representation(value)
        try:
            item = Publisher.objects.get(pk=pk)
            serializer = PublisherSerializer(item)
            return serializer.data
        except Publisher.DoesNotExist:
            return None

    def get_queryset(self):
        return Publisher.objects.all()

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, str(item)) for item in queryset])


class BookSerializer(serializers.ModelSerializer):
    writers = WriterField(many=True)
    publisher = PublisherField(many=False)

    def create(self, validated_data):
        # validated_data['user'] = self.context['request'].user
        validated_data['user'] = get_user_model().objects.get(pk=1)
        writers = validated_data.get('writers')
        del validated_data['writers']

        book = Book.objects.create(**validated_data)
        book.writers.add(*writers)
        return book

    class Meta:
        model = Book
        fields = ['pk', 'title', 'pages', 'publish_year', 'publisher', 'writers', 'creation_date']
