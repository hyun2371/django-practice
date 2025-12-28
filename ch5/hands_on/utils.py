from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def send_str_email(email_to):
    send_mail(
        '새로운 이메일이 도착했습니다.',
        '안녕하세요',
        settings.EMAIL_HOST_USER,
        [email_to],
    )


def send_html_email(email_to):
    subject = "새로운 이메일이 도착했습니다."
    html = render_to_string("email.html")
    message = EmailMessage(
        subject, html,
        settings.EMAIL_HOST_USER,
        [email_to]
    )
    message.content_subtype = "html"
    message.send()
