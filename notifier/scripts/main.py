from notifier import notify_users
from notifier.ad import get_users_data
from notifier.config import configure_logging
from notifier.email import connect_to_server


def main():
    configure_logging()
    notify_users()


if __name__ == '__main__':
    main()
