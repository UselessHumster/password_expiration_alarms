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