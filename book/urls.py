from rest_framework import routers

from .viewsets import BookViewSet

# SimpleRouter() es la clase que define las rutas en nuestro modelo
# Rutas como: get, post, put, patch, delete para generar un restfullAPI
router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls



