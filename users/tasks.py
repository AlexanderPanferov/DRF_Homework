from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone


@shared_task
def deactivate_users():
    """Проверка пользователя на последнее время входа.
       В модели пользователя добавлен флаг is_active.
       Интервал выполнения настраивается в админке"""
    User = get_user_model()
    delta_time = timezone.now() - timezone.timedelta(days=30)
    active_users = User.objects.filter(last_login__lt=delta_time, is_active=True)
    active_users.update(is_active=False)

