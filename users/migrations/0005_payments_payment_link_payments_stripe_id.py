# Generated by Django 4.2.5 on 2024-03-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payments_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
