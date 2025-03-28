# Generated by Django 4.2.7 on 2025-03-28 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0058_reservation_delete_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-order_date'], 'verbose_name': 'Customer Order', 'verbose_name_plural': 'Customer Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='client_email',
            field=models.EmailField(blank=True, default='no-email@example.com', help_text="We'll send your order confirmation here", max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='order',
            name='special_requests',
            field=models.TextField(blank=True, help_text='Any special instructions for your order', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[A-Za-z ]+$', 'Name can only contain letters and spaces')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Phone number must be 10 digits.')]),
        ),
    ]
