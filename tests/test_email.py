from notifier.email import send_email, connect_to_server, prepare_msg
from notifier.config import MAIL_SENDER


def test_send_email():
    server = connect_to_server()
    email = 'test_email@example.com'
    msg = prepare_msg('test', 'Testing', email)
    server.sendmail(MAIL_SENDER, email, msg.as_string())
