from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)
#safe = false means that we can use more than pythin dictionary in the response



@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)

# response can not automatically convert objects to jsonresponse
# but it can do it with python dictionary or lists

# many= true means that there are going to be 
# multiple objects that we need to serialize
# .data will get us rooms in a serialized format

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


# with django api there is a major issue called cors issue
# cross origin resource sharing 
# basically django does not recognize any site that is trying to access our api
# for that we need to specify some or all urls to be used by others and call our api
# we will use django cors headers
