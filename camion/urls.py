from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r"camiones", views.CamionViewSet)
router.register(r"conductor", views.ConductorViewSet)
router.register(r"gastos",views.GastosViewSet)


urlpatterns = [
    #path("", views.index, name="index")
    path('', include(router.urls)),
    path('viajes',views.viajes_count),
]