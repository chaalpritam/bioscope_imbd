from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

from films.models import Film

post_detail_url = HyperlinkedIdentityField(
    view_name='films-api:detail',
    lookup_field='slug'
)

class FilmListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Film
        fields = [
            'pk',
            'url',
            'film_name',
            'display_image',
            'description'
        ]


class FilmDetailSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = [
            'pk',
            'slug',
            'film_name',
            'year',
            'rating',
            'hours_min',
            'genres',
            'release_date',
            'country',
            'user_rating',
            'display_image',
            'banner_image',
            'trailer_link',
            'description',
            'director',
            'writer',
            'stars',
            'metascore',
            'user_review',
            'critic_review',
            'popularity',
            'created_by',
        ]
