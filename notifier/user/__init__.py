from datetime import datetime

from notifier.ad import max_pwd_age
from notifier.config import DAYS_UNTIL_NOTIFICATION, DOMAIN


def normalize_date(date: str):
    timestamp_ms = list(
        filter(
            lambda x: x.isnumeric(), date
        )
    )
    return int("".join(timestamp_ms)) / 1000


def get_name(user):
    return user['SamAccountName']


def get_email(user):
    name = get_name(user)
    return f'{name}@{DOMAIN}'


def get_password_last_set(user):
    pwd_last_set = user['PasswordLastSet']
    if not pwd_last_set:
        return None
    date = normalize_date(pwd_last_set)
    date = datetime.fromtimestamp(date)
    return date


def get_days_until_expire(user):
    pwd_last_set = get_password_last_set(user)
    if not pwd_last_set:
        return None

    today = datetime.today()
    return max_pwd_age - (today - pwd_last_set).days


def is_pwd_expiring(user):
    days_until_exp = get_days_until_expire(user)
    if not days_until_exp:
        return False
    if days_until_exp <= DAYS_UNTIL_NOTIFICATION:
        return True
    return False


def is_expired(user):
    days_until_exp = get_days_until_expire(user)
    if not days_until_exp:
        return True
    if days_until_exp < 0:
        return True
    return False

