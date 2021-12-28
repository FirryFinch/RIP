from movies.models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Movie
        # Поля, которые мы сериализуем
        fields = ["pk", "name", "description", "rating", "is_growing", "date_modified"]