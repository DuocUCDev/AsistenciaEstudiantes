from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsistenciaViewSet, SeccionViewSet, EstudianteViewSet, CursoViewSet, UserViewSet

router = DefaultRouter()
router.register('asistencias', AsistenciaViewSet)
router.register('secciones', SeccionViewSet)
router.register('estudiantes', EstudianteViewSet)
router.register('cursos', CursoViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]