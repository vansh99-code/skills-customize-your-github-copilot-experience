from starter_code import add, divide_numbers, parse_int, calculate_average, unique_word_count


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 4) == 3


def test_divide_numbers():
    assert divide_numbers(5, 2) == 2.5
    assert divide_numbers(10, 4) == 2.5


def test_parse_int():
    assert parse_int("10") == 10
    assert parse_int(" 42 ") == 42


def test_calculate_average():
    assert calculate_average([2, 4, 6]) == 4.0


def test_unique_word_count():
    assert unique_word_count("Hello world hello") == 2
    assert unique_word_count("Python, fastapi. Python!") == 2


def test_parse_int_invalid():
    try:
        parse_int("abc")
        assert False, "Expected ValueError for invalid integer input"
    except ValueError:
        assert True


def test_calculate_average_empty():
    try:
        calculate_average([])
        assert False, "Expected ValueError for empty list"
    except (ValueError, ZeroDivisionError):
        assert True
