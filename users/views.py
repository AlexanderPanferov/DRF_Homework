import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
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
        stripe.api_key = 'sk_test_51Opif0KCIgWCR0iJayl00MseSSZ9ndXRoNNCZNZWRVPJXzG8SiOYViiIF1NtWjZMSHyZeHW5uZhONPpGVeoxUB6y00WhZUmcAS'
        pay = stripe.PaymentIntent.create(
            amount=payment.payment_amount,
            currency='usd',
            automatic_payment_methods={'enabled': True},
        )
        pay.save()
        return super().perform_create(serializer)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


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
