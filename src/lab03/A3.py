def count_freq(tokens: list[str]):
    d = {}
    for word in tokens:
        d[word] = d.get(word, 0) + 1
    return d


test1 = ["a", "b", "a", "c", "b", "a"]
print(count_freq(test1))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    d = {}
    for word in freq:
        d[word] = d.get(word, 0) + 1
    return sorted(d.items(), key=lambda x: (x[1]))[::-1]


test1 = ["bb", "aa", "bb", "aa", "cc"]
print(top_n(test1))
