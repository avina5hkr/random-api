from django.urls import path, include
from rest_framework import routers

from whatsapp import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('validate/', views.validate_api),
    path('api-auth/', include('rest_framework.urls'))
]