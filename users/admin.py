from django.contrib import admin

from users.models import User, Payments

admin.site.register(Payments)
admin.site.register(User)
