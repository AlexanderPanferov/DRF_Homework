from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsListAPIView, UserCreateView, UserListView, UserRetrieveView, UserUpdateView, \
    UserDeleteView, PaymentCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments-list'),
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payments-create'),


    path('create/', UserCreateView.as_view(), name='user-create'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveView.as_view(), name='user-get'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
