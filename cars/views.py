from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializers import CarSerializer
from .models import Car


@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)

    return Response(serializer.data)
