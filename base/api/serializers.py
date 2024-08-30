# these are going to be the classes that take an object or a certain model
# and turn it into json data
# basically python object -> json object

from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    class Meta: 
        model = Room
        fields = '__all__'
# this take all the fields from Room model in base and serialize it 

