from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django.db.models.signals import post_save
from django.dispatch import receiver

from watcheck import settings

UserModel = get_user_model()


def send_email_registration(user):
    send_mail(
        "Registration greetings",
        "Welcome to the best watches shop",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=UserModel)
def user_create(instance, created, **kwargs):
    if created:
        send_email_registration(instance)
