from rest_framework.generics import ListAPIView, RetrieveAPIView
from films.models import Film
from .serializers import (
    FilmListSerializer,
    FilmDetailSerializer,
    )

class FilmListAPIView(ListAPIView):
    serializer_class = FilmListSerializer
    queryset = Film.objects.all()


class FilmDetailAPIView(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer
    lookup_field = "slug"
