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
Dear {instance.first_name},

We are excited to welcome you to Collaborator, the ultimate tool for shared to-do lists. Whether you're managing a team, planning a project, or simply organizing your personal tasks, Collaborator makes it easy to collaborate and stay on track.

To get started, simply log in to your account using the email address and password you provided during registration. Once you're in, you'll be able to create and share tasks with your collaborators, set due dates, and track progress in real time.

If you need any help getting started or have any questions, please don't hesitate to contact our support team. We're here to help you make the most of Collaborator and ensure your success.

Thank you for joining us on this exciting journey. We look forward to helping you achieve your goals and stay organized with Collaborator.

Best regards,

Collaborator Team
            """,
            from_email=None,
            recipient_list=[instance.email]
        )
    return None