from typing.io import TextIO
from datetime import datetime
from constants import FILE_NAME_LOG


log_file: TextIO


def open_log_file() -> None:
    global log_file
    log_file = open(FILE_NAME_LOG, 'a', encoding='utf-8')
    text = f'{get_datetime()}   Игра начата\n'
    write_log(text)


def write_log(text) -> None:
    global log_file
    log_file.write(text)


def get_datetime() -> str:
    date = datetime.today()
    date = date.strftime('%Y.%m.%d  %H:%M')
    return date


def close_log_file() -> None:
    global log_file
    text = f'{get_datetime()}   Игра окончена\n\n'
    log_file.write(text)
    log_file.close()
