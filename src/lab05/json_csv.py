import json
import csv
from pathlib import Path


def json_to_csv(src_path: str, dst_path: str) -> None:
    """Конвертирует JSON файл в CSV файл."""
    input_path = Path(src_path)
    output_path = Path(dst_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {src_path}")

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("JSON файл некорректен")

    if not data or not isinstance(data, list):
        raise ValueError("JSON файл пуст или некорректен")

    # Получаем ключи из первого элемента
    fieldnames = list(data[0].keys())

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(src_path: str, dst_path: str) -> None:
    """Конвертирует CSV файл в JSON файл."""
    input_path = Path(src_path)
    output_path = Path(dst_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Файл не найден: {src_path}")

    data = []
    with open(input_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    if not data:
        raise ValueError("CSV файл пуст или некорректен")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
