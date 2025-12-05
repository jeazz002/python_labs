import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    pattern = r"[^\s]+"
    normalized = []
    for match in re.finditer(pattern, text):
        normalized.append(match.group())

    return " ".join(normalized).strip()


import re


def tokenize(text: str) -> list[str]:
    pattern = r"[\w-]+"
    tokens = []
    for match in re.finditer(pattern, text):
        tokens.append(match.group())

    return tokens


def count_freq(tokens: list[str]):
    d = {}
    for word in tokens:
        d[word] = d.get(word, 0) + 1
    return d


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # Сортируем по убыванию частоты, при равных частотах - по алфавиту
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

