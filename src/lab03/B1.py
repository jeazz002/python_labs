import sys
from lib import text

line = sys.stdin.readline()
tokenized = text.tokenize(line)
unique_words = text.top_n(tokenized)
result = text.count_freq(unique_words)
print(f"Всего слов: {len(tokenized)}")
print(f"Уникальных слов: {len(unique_words)}")
print("top-5:")
for string in result:
    print(f"{string[0]}:{string[1]}")
