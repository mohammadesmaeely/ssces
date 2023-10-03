from rest_framework.routers import DefaultRouter

from events.views.event_category import EventCategoryReadViewSet
from events.views.evnet import EventViewSet
from events.views.registered_event import RegisteredEventView

router = DefaultRouter()

router.register('event_categories', EventCategoryReadViewSet)
router.register('events', EventViewSet)
router.register('registered_event', RegisteredEventView)

urlpatterns = [

] + router.urls
