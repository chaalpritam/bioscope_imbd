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
    serializer_class = FilmDetailSerializer
    queryset = Film.objects.all()
    lookup_field = "slug"
