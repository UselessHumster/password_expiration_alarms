from notifier.config import ALARM_TEMPLATE, AD_DOMAIN

from notifier.user import (
    get_days_until_expire,
    get_name
)


def get_correct_ending(count: int):
    last_char_of_day = str(count)[-1]
    correct_endings = {'день': ['день', 'дня', 'дней']}
    index_word_end_by_1 = 0
    index_word_end_by_2_3_4 = 1
    index_word_end_else = 2

    if count in [11, 12, 13, 14]:
        return correct_endings['день'][index_word_end_else]
    elif last_char_of_day == '1':
        return correct_endings['день'][index_word_end_by_1]
    elif last_char_of_day in ['2', '3', '4']:
        return correct_endings['день'][index_word_end_by_2_3_4]
    return correct_endings['день'][index_word_end_else]


def generate_alarm_txt(_user):
    expires_in = get_days_until_expire(_user)
    name = get_name(_user)
    days_caption = get_correct_ending(expires_in)
    return f'Добрый день! ' \
           f'Пароль от учетной записи {AD_DOMAIN}\\{name} ' \
           f'истекает через {expires_in} {days_caption} ' \
           f'{ALARM_TEMPLATE}'
