from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from materials.models import Course, Lesson, Subscription
from materials.paginators import LessonPaginator, CoursePaginator
from materials.serializers import CourseSerializer, LessonSerializer, CourseListSerializer, SubSerializer
from users.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    default_serializer = CourseSerializer
    pagination_class = CoursePaginator

    serializers = {
        "list": CourseListSerializer,
        "retrieve": CourseListSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        permissions_map = {
            'create': [IsAuthenticated, ~IsModerator],
            'list': [IsAuthenticated, IsModerator | IsOwner],
            'retrieve': [IsAuthenticated, IsModerator | IsOwner],
            'update': [IsAuthenticated, IsModerator | IsOwner],
            'partial_update': [IsAuthenticated, IsModerator | IsOwner],
            'destroy': [IsAuthenticated, IsOwner]
        }
        self.permission_classes = permissions_map.get(self.action, [])
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonDetailView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
    pagination_class = LessonPaginator


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsModerator]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class SubViewSet(viewsets.ModelViewSet):
    serializer_class = SubSerializer
    queryset = Subscription.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

