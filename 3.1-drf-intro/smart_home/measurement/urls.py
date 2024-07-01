from django.urls import path

from .views import GetCreateSensor, UpdateSensor


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', GetCreateSensor.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view())
]
