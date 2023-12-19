import pytest

from coursework.tolls import *


@pytest.mark.parametrize(
    "date, expected_result",
    [
        ("2020-08-12T02:26:18.671407", "12.08.2020"),
        ("2019-01-20T02:26:18.671407", "20.01.2019"),
        ("2016-05-01T02:26:18.671407", "01.05.2016"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_convert_data(date: str, expected_result: str) -> Any:
    """Test для функции convert_data"""
    assert convert_data(date) == expected_result


@pytest.mark.parametrize(
    "input_st, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_hides_data(input_st: str, expected_result: str) -> Any:
    """Test для функции hides_data"""
    assert hides_data(input_st) == expected_result


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_number_card(number: str, expected_result: str) -> Any:
    assert number_card(number) == expected_result


@pytest.mark.parametrize(
    "account, expected_result",
    [("73654108430135874305", "**4305"), ("35383033474447895560", "**5560"), ("64686473678894779589", "**9589")],
)
def test_account_number(account: str, expected_result: str) -> Any:
    assert account_number(account) == expected_result


@pytest.fixture
def my_data() -> list[dict[str, object]]:
    """Создание фикстуры"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_data(my_data: list[dict[str, object]]) -> Any:
    """Тест для проверки функции sort_data"""
    assert sort_date(my_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]