

from rest_framework.routers import DefaultRouter

from flights_app.views.order import OrderViewSet

router = DefaultRouter()
router.register('', OrderViewSet, basename='order')


urlpatterns = []


urlpatterns.extend(router.urls)

