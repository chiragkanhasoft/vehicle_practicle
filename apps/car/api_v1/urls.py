from rest_framework import routers

from apps.car.api_v1 import views

router = routers.SimpleRouter()
router.register("car", views.CarModelViewSet)
router.register("rate", views.RatingModelViewSet)
router.register("popular", views.PopulerModelViewSet)

app_name = "car"
urlpatterns = [] + router.urls
