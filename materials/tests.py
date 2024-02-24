from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='admin@admin.com',
            is_staff=True,
            is_superuser=True,
        )
        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test',
            description='Testing'
        )
        self.lesson = Lesson.objects.create(
            title='test1',
            description='testing1',
            course=self.course,
            user=self.user
        )

    def test_create_lesson(self):
        """Тест создания урока"""
        data = {
            'title': 'Test',
            'description': 'Testing',
            'course': self.course.pk,
            'user': self.user.pk
        }
        response = self.client.post(
            reverse('materials:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'title': 'Test', 'description': 'Testing', 'preview': None, 'link': None,
             'course': self.course.pk, 'user': self.user.pk}
        )
        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_get_list(self):
        """Тест списка уроков"""
        response = self.client.get(
            reverse('materials:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.pk, 'title': 'test1', 'description': 'testing1', 'preview': None, 'link': None,
                 'course': self.course.pk, 'user': self.user.pk}]}

        )

    def test_update_lesson(self):
        """Тест обнавления урока"""
        data = {
            'title': 'Test',
            'description': 'Testing',
            'course': self.course.pk,
            'user': self.user.pk
        }

        response = self.client.put(
            reverse('materials:lesson-update', kwargs={'pk': self.lesson.pk}),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тест удаления урока"""

        response = self.client.delete(
            reverse('materials:lesson-delete', kwargs={'pk': self.lesson.pk})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='admin@admin.com',
            is_staff=True,
            is_superuser=True,
        )
        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test',
            description='Testing'
        )
        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
            is_active=True,
        )

    def test_create_subscription(self):
        """Тест создания подписки"""
        data = {
            'user': self.user.pk,
            'course': self.course.pk,
            'is_active': True
        }

        response = self.client.post(
            reverse('materials:subscription-list'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'is_active': True, 'user': self.user.pk, 'course': self.course.pk}

        )

    def test_list_subscription(self):
        """Тест списка подписок"""
        response = self.client.get(
            reverse('materials:subscription-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': self.subscription.pk, 'is_active': True, 'user': self.user.pk, 'course': self.course.pk}]

        )

    def test_update_subscription(self):
        """Тест обнавления подписки"""
        new_course = Course.objects.create(title='New Course')
        response = self.client.patch(
            reverse('materials:subscription-detail', args=[self.subscription.pk]),
            data={'course': new_course.pk},
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


def test_delete_subscription(self):
    """Тест удаления подписки"""

    response = self.client.delete(
        reverse('materials:subscription-detail', args=[self.subscription.pk]),
    )

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
