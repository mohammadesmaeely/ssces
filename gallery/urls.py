from rest_framework.routers import DefaultRouter

from gallery.views.gallery_image import GalleryImageReadViewSet

router = DefaultRouter()

router.register('gallery_images', GalleryImageReadViewSet)


urlpatterns = [

] + router.urls

