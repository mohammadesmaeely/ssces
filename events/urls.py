from rest_framework.routers import DefaultRouter

from events.views.anonymous_registered_event import AnonymousRegisteredEventView
from events.views.event_category import EventCategoryReadViewSet
from events.views.evnet import EventViewSet
from events.views.registered_event import RegisteredEventView

router = DefaultRouter()

router.register('event_categories', EventCategoryReadViewSet)
router.register('events', EventViewSet)
router.register('registered_event', RegisteredEventView)
router.register('anonymous_registered_event', AnonymousRegisteredEventView)

urlpatterns = [

] + router.urls
