from rest_framework.routers import DefaultRouter

from cooperation.views.cooper_reply import CooperationReplyView
from cooperation.views.cooperation_form import CooperationFormReadViewSet

router = DefaultRouter()

router.register('cooperation_forms', CooperationFormReadViewSet)
router.register('cooperation_replies', CooperationReplyView)

urlpatterns = [

] + router.urls
