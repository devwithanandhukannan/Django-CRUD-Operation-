from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreate, CategoryDetail, CourseViewSet

# Router for Course ModelViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    # Category endpoints (APIView)
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # Include Course router endpoints (ModelViewSet)
    path('', include(router.urls)),
]
