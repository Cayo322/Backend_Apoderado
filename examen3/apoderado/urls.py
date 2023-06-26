from rest_framework.routers import DefaultRouter
from django.urls import path

from . import views

router = DefaultRouter()

router.register(r'parentesco',
                views.ParentescoViewSet,
                basename='parentesco')
router.register(r'apoderado',
                views.ApoderadoViewSet,
                basename='apoderado')

urlpatterns = router.urls