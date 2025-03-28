from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, Table, Reservation


@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    """
    Send email confirmation when a new order is placed.
    Includes both plain text and HTML versions.
    """
    if created and instance.client_email:  # Only send for new orders with email
        try:
            subject = f"📦 Order Confirmation #{instance.id} - {settings.SITE_NAME}"

            # Context for email templates
            context = {
                'order': instance,
                'site_name': settings.SITE_NAME,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'contact_phone': settings.CONTACT_PHONE,
            }

            # Render both text and HTML versions
            text_content = render_to_string('emails/order_confirmation.txt', context)
            html_content = render_to_string('emails/order_confirmation.html', context)

            # Create and send email
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[instance.client_email],
                reply_to=[settings.REPLY_TO_EMAIL],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

        except Exception as e:
            # Log the error but don't crash the application
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to send order confirmation email: {str(e)}")


@receiver(post_save, sender=Table)
def send_reservation_confirmation(sender, instance, created, **kwargs):
    """
    Send email confirmation when a table is reserved.
    Checks for associated reservation before sending.
    """
    if created and hasattr(instance, 'reservation'):
        try:
            reservation = instance.reservation
            subject = f"🍽️ Reservation Confirmed - {settings.SITE_NAME}"

            context = {
                'reservation': reservation,
                'table': instance,
                'site_name': settings.SITE_NAME,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'contact_phone': settings.CONTACT_PHONE,
            }

            text_content = render_to_string('emails/reservation_confirmation.txt', context)
            html_content = render_to_string('emails/reservation_confirmation.html', context)

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[reservation.email],
                reply_to=[settings.REPLY_TO_EMAIL],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Failed to send reservation confirmation email: {str(e)}")