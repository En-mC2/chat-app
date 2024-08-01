from base.models import Room
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RoomSerializer
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api/',
        'GET/api/rooms',
        'GET/api/rooms/:id',
        
    ]
    return Response(routes)
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(['GET'])
def getRooms1(request,pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializer(rooms, many=False)
    print(serializer)
    return Response(serializer.data)