from django.urls import path
from flights_app import views



from rest_framework.routers import DefaultRouter

from flights_app.views.flight import FlightsViewSet

router = DefaultRouter()
router.register('', FlightsViewSet, basename='flight')


urlpatterns = []


urlpatterns.extend(router.urls)














