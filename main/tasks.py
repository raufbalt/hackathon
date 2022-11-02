from .celery import app
from account.send_email import send_confirmation_email


@app.task
def send_email_task(user, code):
    send_confirmation_email(user, code=code)

