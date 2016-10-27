from rest_framework.serializers import ModelSerializer
from films.models import Film
from rest_framework.serializers import HyperlinkedIdentityField

post_detail_url = HyperlinkedIdentityField(
    view_name = 'films-api:detail',
    lookup_field = 'slug'

)

class FilmDetailSerializer(ModelSerializer):

    class Meta:
        model = Film
        fields = [
            'pk',
            'film_name',
            'year',
            'raring',
            'hours_min',
            'genres',
            'release_date',
            'country',
            'user_rating',
            'display_image',
            'banner_image',
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
