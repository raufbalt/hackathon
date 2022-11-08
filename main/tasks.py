from account.models import Spam_Contacts
from .celery import app
from django.core.mail import send_mail

@app.task
def send_email_task(user, code):
    full_link = f'http://34.67.85.209/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт.',
        f'Чтобы активировать аккаунт, аам необходимо перейти по ссылке: {full_link}',
        'kutmanvip01@gmail.com',
        [user],
        fail_silently=False,
    )


@app.task
def send_spam_email():
    for user in Spam_Contacts.objects.all():
        send_mail(
            'Spam Spam Spam',
            'This is spam letter for you by Kutman!',
            'kutmanvip01@gmail.com',
            [user.email],
            fail_silently=False,
        )
# автоматически запускать с помощью супервизор
