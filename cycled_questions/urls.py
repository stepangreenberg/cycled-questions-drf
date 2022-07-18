from rest_framework.routers import SimpleRouter
from .views import CreatureViewSet, QuestionViewSet

router = SimpleRouter()

router.register('creature', CreatureViewSet, basename='creature')
router.register('question', QuestionViewSet, basename='question')

urlpatterns = router.urls
