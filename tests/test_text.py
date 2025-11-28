import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("Привет\nМИp\t", "привет миp"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        (" двойные пробелы ", "двойные пробелы"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello world", ["hello", "world"]),
        ("", []),
        ("hello, world!", ["hello", "world"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


def test_count_freq_and_top_n():
    tokens = ["яблоко", "банан", "яблоко", "апельсин"]
    freq = count_freq(tokens)
    assert freq["яблоко"] == 2
    assert freq["банан"] == 1

    top = top_n(freq, 2)
    assert len(top) == 2


def test_top_n_tie_breaker():
    freq = {"яблоко": 3, "банан": 3, "апельсин": 3}
    result = top_n(freq, 3)
    # При равной частоте сортировка по алфавиту
    assert result[0][0] == "апельсин"
    assert result[1][0] == "банан"
    assert result[2][0] == "яблоко"
