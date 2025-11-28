import re


def tokenize(text: str) -> list[str]:
    pattern = r"[\w]+(?:-[\w]+)*"
    tokens = []
    for match in re.finditer(pattern, text):
        tokens.append(match.group())

    return tokens


test_cases = [
    "привет мир-=",
    "hello,world!!!",
    "по-настоящему круто",
    "2025 год",
    "emoji 😀 не слово",
]
for test in test_cases:
    result = tokenize(test)
    print(result)
