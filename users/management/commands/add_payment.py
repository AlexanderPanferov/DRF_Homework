from datetime import datetime
from decimal import Decimal

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payments, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        user = User.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()


        Payments.objects.create(
            user=user,
            date_payment=datetime.now(),
            paid_course=course,
            paid_lesson=lesson,
            payment_amount=Decimal('50.00'),
            payment_method='card'
        )

        self.stdout.write(self.style.SUCCESS('Payments data created successfully'))