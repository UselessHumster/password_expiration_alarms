from notifier.email import send_email, connect_to_server
from notifier.user import (
    get_days_until_expire,
    get_name,
    is_expired,
    is_pwd_expiring,
    get_users_to_notify
)
from notifier.utils import get_correct_ending


def notify_users():
    server = connect_to_server()
    users = get_users_to_notify()
    for _user in users:
        send_email(server, _user)
    server.quit()
