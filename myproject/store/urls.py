from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LessonViewSet, UserBalanceViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'userbalance', UserBalanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]