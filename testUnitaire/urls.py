from django.urls import path, include
from . import views

from testUnitaire.models import Games
from rest_framework import routers, serializers, viewsets


# Serializer
class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = "__all__"


# ViewSets
class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


# Routers
router = routers.DefaultRouter()
router.register(r"games", GamesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("home/", views.home, name="home"),
]
