from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth.models import User
from django.core.mail import send_mail

# receives signal from Django when a new user account is created and
# sends welcome email
@receiver(signals.post_save, sender=User)
def NewUserConfirmationEmail(instance, created, **kwargs):
    if (created == True):
        send_mail(
            subject="Welcome to Collaborator!",
            message=f"""
            {instance.first_name}, 
            Welcome to the Collaborator ToDo program!
            """,
            from_email=None,
            recipient_list=[instance.email]
        )
    return None