from rest_framework.serializers import  (
    ModelSerializer,
    HyperlinkedIdentityField,
    )

from films.models import Film



post_detail_url = HyperlinkedIdentityField(
    view_name = 'films-api:detail',
    lookup_field = 'slug'
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
            'film_name',
            'display_image',
            'description',
            'year',
            'genres',
            'rating',
            'hours_min',
            'user_rating',
            'director',
            'writer',
            'metascore',
            'user_reviews',
            'critic_review',
            'popularity',
            'stars',
            'country',
            'banner_image',
            'display_image',
            'release_date',
        ]
