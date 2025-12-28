from django.core.mail import send_mail
from django.conf import settings

def send_str_email(email_to):
    send_mail(
        '새로운 이메일이 도착했습니다.',
        '안녕하세요',
        settings.EMAIL_HOST_USER,
        [email_to],
    )