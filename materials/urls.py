from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateView, LessonListView, LessonDetailView, LessonUpdateView, \
    LessonDestroyView, SubViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'subscription', SubViewSet, basename='subscription')

urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/', LessonListView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson-delete'),
] + router.urls
