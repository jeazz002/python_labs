from pathlib import *
import sys

current_file = Path(__file__)
print(f"Текущий файл: {current_file}")

parent_dir = current_file.parent.parent
sys.path.append(str(parent_dir))
from lib.io_txt_csv import read_text, write_csv
from lib.text import frequencies_from_text, sorted_word_counts

input_file = "src/Data/input_test.txt"
output_file = "src/Data/output.csv"
encoding = "utf-8"
input_path = Path(input_file)
output_path = Path(output_file)
if not input_path.exists():
    print(f"Ошибка: Файл '{input_file}' не найден.")
    print("Пожалуйста, проверьте правильность пути к файлу.")
else:
    try:
        file = read_text(input_file, encoding)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"Ошибка декодирования: проверьте кодировку (сейчас encoding='{encoding}')."
        )
        sys.exit(1)

    freq = frequencies_from_text(file)
    sorted_words = sorted_word_counts(freq)

    csv_rows = [[word, count] for word, count in sorted_words]
    csv_header = ("word", "count")
    write_csv(csv_rows, output_path, csv_header)
    total_words = sum(freq.values())
    unique_words = len(freq)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ 5 самых частых слов:")

    top_5 = sorted_words[:5]
    if top_5:
        for i, (word, count) in enumerate(top_5):
            print(f"  {i+1}. '{word}': {count}")
