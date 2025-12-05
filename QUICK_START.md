# Быстрый старт lab08

## Способ 1: Готовый скрипт (самый простой)

```bash
python run_lab08.py
```

## Способ 2: Интерактивно в Python

```python
import sys
from pathlib import Path

# Добавляем src в путь
sys.path.insert(0, str(Path.cwd() / "src"))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

# Создание студента
student = Student(
    fio="Иванов Иван Иванович",
    birthdate="2000-05-15",
    group="SE-01",
    gpa=4.5
)

print(student)  # Иванов Иван Иванович, гр. SE-01, GPA 4.50
print(f"Возраст: {student.age()} лет")

# Сохранение в JSON
students = [student]
students_to_json(students, "src/lab08/data/test.json")

# Загрузка из JSON
loaded = students_from_json("src/lab08/data/students_input.json")
for s in loaded:
    print(s)
```

## Способ 3: Свой скрипт

Создайте файл `my_script.py` в корне проекта:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

# Ваш код
student = Student("Петров Пётр", "2001-03-20", "IKBO-12", 4.2)
print(student)
```

Запуск: `python my_script.py`

