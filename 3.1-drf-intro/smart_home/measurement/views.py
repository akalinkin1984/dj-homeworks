from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView

from .serializers import SensorsSerializer
from .models import Sensor


class GetCreateSensor(ListAPIView, CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateSensor(RetrieveUpdateAPIView, pk):
    queryset = Sensor.objects.filter(id=pk)

