from django.urls import path

from .views import GetCreateSensor, GetUpdateSensor, AddMeasurement


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', GetCreateSensor.as_view()),
    path('sensors/<pk>/', GetUpdateSensor.as_view()),
    path('measurements/', AddMeasurement.as_view())
]
