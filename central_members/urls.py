from rest_framework.routers import DefaultRouter

from central_members.views.central_member import CentralMemberReadViewSet
from central_members.views.council_period import CouncilPeriodReadViewSet

router = DefaultRouter()

router.register('council_periods', CouncilPeriodReadViewSet)
router.register('central_members', CentralMemberReadViewSet)

urlpatterns = [

] + router.urls
