import stripe
from django.conf import settings


def stripe_session(payment):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Создание продукта
    product = stripe.Product.create(name=payment.paid_course)

    # Создание цены
    price = stripe.Price.create(
        product=product.id,
        unit_amount=payment.payment_amount * 100,
        currency='usd'
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

    return session
