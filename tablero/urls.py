from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from tablero import views

router = DefaultRouter()
router.register(r'tableros', views.TableroViewSet)
router.register(r'columnas', views.ColumnaViewSet)
router.register(r'tareas', views.TareaViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/', include(router.urls)),

    # autenticacion (Evaluacion 3): uso las vistas que ya trae Django,
    # solo les doy mi propio template
    path('login/', auth_views.LoginView.as_view(template_name='tablero/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # vistas protegidas
    path('panel/', views.panel_funcion, name='panel-funcion'),
    path('panel-clase/', views.PanelClaseView.as_view(), name='panel-clase'),
]
