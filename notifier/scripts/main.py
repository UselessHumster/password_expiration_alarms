from notifier import notify_users
from notifier.ad import get_data
from notifier.config import configure_logging
from notifier.email import connect_to_server


def main_loop():
    configure_logging()
    server = connect_to_server()
    notify_users(server, get_data())
    server.quit()


if __name__ == '__main__':
    main_loop()
