from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт.',
        f'Чтобы активировать аккаунт, аам необходимо перейти по ссылке: {full_link}',
        'kutmanvip01@gmail.com',
        [user],
        fail_silently=False,
    )



def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Письмо с кодом для сброса пароля!',
        f'Ваш код для востановления: {code}',
        'abdb2226@gmail.com',
        [user],
        fail_silently=False
    )