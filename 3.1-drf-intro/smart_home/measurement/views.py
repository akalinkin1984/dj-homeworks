from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor


# получение списка датчиков / создание датчика
class GetCreateSensor(ListAPIView, CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# изменение датчика / получение информации о конкретном датчике
class GetUpdateSensor(RetrieveUpdateAPIView, APIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        ser = SensorDetailSerializer(sensor)
        return Response(ser.data)


# добавить измерение
class AddMeasurement(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
