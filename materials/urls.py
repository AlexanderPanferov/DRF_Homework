from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateView, LessonListView, LessonDetailView, LessonUpdateView, \
    LessonDestroyView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('create/', LessonCreateView.as_view(), name='lesson-create'),
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lesson-get'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson-delete'),
] + router.urls
