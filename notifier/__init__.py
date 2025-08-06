from notifier.config import ALARM_TEMPLATE
from notifier.email import send_email
from notifier.user import (
    get_days_until_expire,
    get_name,
    is_expired,
    is_pwd_expiring,
)
from notifier.utils import get_correct_ending


def generate_alarm_txt(_user):
    expires_in = get_days_until_expire(_user)
    name = get_name(_user)
    days_caption = get_correct_ending(expires_in)
    return f'Добрый день! ' \
           f'Пароль от учетной записи alkaloidad\\{name} ' \
           f'истекает через {expires_in} {days_caption} ' \
           f'{ALARM_TEMPLATE}'


def notify_users(server, users):
    for _user in users:
        if not is_pwd_expiring(_user):
            continue

        if is_expired(_user):
            continue

        send_email(server, _user)
