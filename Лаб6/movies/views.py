from rest_framework import viewsets
from movies.serializers import MovieSerializer
from movies.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Movie.objects.all().order_by('date_modified')
    serializer_class = MovieSerializer  # Сериализатор для модели