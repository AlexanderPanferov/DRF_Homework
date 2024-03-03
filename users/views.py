import stripe
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Payments, User
from users.serializers import PaymentsSerializer, UserSerializer, UserCreateSerializer


class PaymentsListAPIView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payment_method', 'paid_lesson', 'paid_course')
    ordering_fields = ('date_payment',)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save()
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Создание продукта
        product = stripe.Product.create(name=payment.paid_course)

        # Создание цены
        price = stripe.Price.create(
            product=product.id,
            unit_amount=payment.payment_amount,
            currency='usd',
        )

        # Создание сессии
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price.id,
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://http://127.0.0.1:8000/{CHECKOUT_SESSION_ID}',

        )

        serializer.save(stripe_id=session.id, payment_link=session.url)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
