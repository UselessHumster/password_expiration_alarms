import logging
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from notifier import generate_alarm_txt
from notifier.config import (
    EMAIL_PASSWORD,
    EMAIL_SERVER,
    EMAIL_USERNAME,
    MAIL_SENDER,
)
from notifier.user import get_days_until_expire, get_email
from notifier.utils import get_correct_ending


def connect_to_server():
    logging.info('Trying to connect to SMTP...')
    server = smtplib.SMTP(EMAIL_SERVER)
    server.starttls()
    server.ehlo()
    server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    status_code, _ = server.noop()
    if status_code == 250:
        logging.info(f'Successfully connected to {server=}')
        return server
    logging.error(f"Can't connect to the server, status code {status_code}")


def send_email(server, user):
    msg = get_mail_msg(user)
    user_email = get_email(user)
    if not msg:
        return None
    logging.info(f'Sending email to the {user_email}')
    try:
        server.sendmail(MAIL_SENDER, user_email, msg.as_string())
    except Exception as e:
        logging.error(f'Email not sent with error {e}')
    else:
        logging.info('Email successfully sent')


def get_mail_msg(user):
    expires_in = get_days_until_expire(user)
    if not expires_in:
        return None
    days_caption = get_correct_ending(expires_in)
    subject = f'Ваш пароль истекает через {expires_in} {days_caption}'
    body = generate_alarm_txt(user)
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['To'] = get_email(user)
    return msg
