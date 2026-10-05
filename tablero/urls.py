from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tablero import views

router = DefaultRouter()
router.register(r'tableros', views.TableroViewSet)
router.register(r'columnas', views.ColumnaViewSet)
router.register(r'tareas', views.TareaViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/', include(router.urls)),
]
