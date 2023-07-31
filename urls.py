from django.urls import path, include
from rest_framework import routers

from miningusage import views
from miningusage.views import WebpageViewSet

router = routers.DefaultRouter()
router.register(r'webPage', WebpageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

