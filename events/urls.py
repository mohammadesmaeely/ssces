from rest_framework.routers import DefaultRouter

from events.views.event_category import EventCategoryReadViewSet
from events.views.evnet import EventViewSet

router = DefaultRouter()

router.register('event_categories', EventCategoryReadViewSet)
router.register('events', EventViewSet)

urlpatterns = [

] + router.urls
