from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView

from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


# получение списка датчиков / создание датчика
class GetCreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# изменение датчика / получение информации о конкретном датчике
class GetUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# добавить измерение
class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
