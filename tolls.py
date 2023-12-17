from datetime import datetime

from typing import Any


def check_dict(data: list[Any], state: str = "EXECUTED") -> list[Any]:
    """
    Функия возвращает список словарей с определеным ключем
    :param data: list
    :param state: str
    :return: list
    """
    result = []
    for diction in data:
        if "state" in diction and diction["state"] == state:
            result.append(diction)
    return result


def sort_date(data: list[Any], sort: bool = True) -> list[Any]:
    """
    Функия возвращает отсортированый по дате список словарей
    :param data: list
    :param sort: list
    :return: list
    """
    data = filter(lambda x: "date" in x, data)
    return sorted(data, key=lambda x: x["date"], reverse=sort)


def convert_data(data: str) -> str:
    """Преобразование строки в объект даты и времени
    Формат строки включает миллисекунды, поэтому нужно использовать формат "%f" для них"""
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    return datetime.strptime(data, date_format).strftime("%d.%m.%Y")


def number_card(user_card: str) -> str:
    """
    Функция для маскировки номера карты
    """
    return user_card[:4] + " " + user_card[4:6] + "** ****" + " " + user_card[-4:]


def account_number(user_account: str) -> str:
    """
    Функция для маскировки номера счета
    """
    return "**" + user_account[-4:]


def hides_data(input_str: str) -> str:
    """
    Функция возвращает тип карты/счета и скрытый номер карты/счета
    :param input_str: str
    :return: str
    """
    input_lst = input_str.split(" ")
    if input_lst[0] == "Счет":
        return str(input_lst[0] + " " + account_number(input_lst[1]))
    else:
        return str(" ".join(input_lst[:-1]) + " " + number_card(input_lst[-1]))