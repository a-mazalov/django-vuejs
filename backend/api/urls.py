from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    PostViewSet,
    CourseViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = router.urls
