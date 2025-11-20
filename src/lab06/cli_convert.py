import argparse
import sys
from pathlib import Path

current_file = Path(__file__)
parent_dir = current_file.parent.parent
sys.path.insert(0, str(parent_dir))

import importlib.util

def load_module(filename):
    module_path = parent_dir / "lab05" / filename
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

json_csv = load_module("json---csv.py")
csv_json = load_module("csv---json.py")
csv_xlsx = load_module("csv---xlxs.py")

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            input_path = Path(args.input)
            if not input_path.exists():
                parser.error(f"Файл не найден: {input_path}")
            json_csv.json_to_csv(args.input, args.output)
        elif args.cmd == "csv2json":
            input_path = Path(args.input)
            if not input_path.exists():
                parser.error(f"Файл не найден: {input_path}")
            csv_json.csv_to_json(args.input, args.output)
        elif args.cmd == "csv2xlsx":
            input_path = Path(args.input)
            if not input_path.exists():
                parser.error(f"Файл не найден: {input_path}")
            csv_xlsx.csv_to_xlsx(args.input, args.output)
    except FileNotFoundError as e:
        parser.error(str(e))
    except Exception as e:
        parser.error(f"Ошибка: {e}")

if __name__ == "__main__":
    main()