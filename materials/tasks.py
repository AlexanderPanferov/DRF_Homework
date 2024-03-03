from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from materials.models import Subscription, Course


@shared_task
def send_mail_course_update(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course__id=course_id, is_active=True)
    send_mail(
        subject=f"Обновление курса: {course.title}",
        message=f"Курс '{course.title}' был обновлен",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=subscriptions.values_list('user__email', flat=True)
    )

