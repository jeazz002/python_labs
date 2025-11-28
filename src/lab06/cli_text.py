import argparse
import sys
from pathlib import Path

current_file = Path(__file__)
parent_dir = current_file.parent.parent
sys.path.insert(0, str(parent_dir))

from lab03.lib.text import tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        input_path = Path(args.input)
        if not input_path.exists():
            parser.error(f"Файл не найден: {input_path}")

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            parser.error(f"Ошибка при чтении файла: {e}")

        for i, line in enumerate(lines, start=1):
            if args.n:
                print(f"{i:6d}  {line}", end="")
            else:
                print(line, end="")

    elif args.command == "stats":
        input_path = Path(args.input)
        if not input_path.exists():
            parser.error(f"Файл не найден: {input_path}")

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            parser.error(f"Ошибка при чтении файла: {e}")

        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, args.top)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(freq)}")
        print(f"Топ-{args.top}:")
        for word, count in top_words:
            print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
