import logging
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
DOMAIN = os.getenv("domain")
AD_DOMAIN = os.getenv("ad_domain")
ALARM_TEMPLATE = open('.\\alarm_template.txt', encoding='utf-8').read()
MAIL_SENDER = os.getenv("mail_sender")
EMAIL_USERNAME = MAIL_SENDER
EMAIL_PASSWORD = os.getenv("email_password")
OU_PATH = os.getenv("ou_path")
EMAIL_SERVER = os.getenv("smtp_server")
DAYS_UNTIL_NOTIFICATION = 7


def configure_logging():
    today = datetime.now().__format__("%Y-%m-%d")
    logging.basicConfig(level=logging.INFO,
                        filename=f'Logs/unlock_bot_{today}.log',
                        filemode='a',
                        format='[%(asctime)s]:%(levelname)s:\t%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
