from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order, Table

@receiver(post_save, sender=Order)
def order_notification(sender, instance, created, **kwargs):
    """Send email notification when an order is successfully placed."""
    if created:
        send_mail(
            subject="Order Confirmation",
            message=f"Dear {instance.customer}, your order for {instance.foodname} has been received!",
            from_email="yourrestaurant@example.com",
            recipient_list=[instance.customer.email],  # Ensure Customer model has an email field
            fail_silently=True,
        )

@receiver(post_save, sender=Table)
def reservation_notification(sender, instance, created, **kwargs):
    """Send email notification when a table reservation is successful."""
    if created:
        send_mail(
            subject="Table Reservation Confirmed",
            message=f"Dear {instance.customer}, your table reservation for {instance.date} is confirmed!",
            from_email="yourrestaurant@example.com",
            recipient_list=[instance.customer.email],
            fail_silently=True,
        )
