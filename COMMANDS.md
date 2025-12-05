# Команды для запуска lab08

## ⚡ Быстрый запуск (самый простой способ)

### Windows (PowerShell или CMD):
```bash
cd C:\Users\semen\.ssh\python_labs
python run_lab08.py
```

### Если вы уже в корне проекта:
```bash
python run_lab08.py
```

---

## 📝 Все доступные команды

### 1. Запуск демонстрационного скрипта
```bash
python run_lab08.py
```

### 2. Альтернативный тестовый скрипт
```bash
python test_lab08.py
```

### 3. Интерактивный Python (для экспериментов)
```bash
python
```

Затем в Python выполните:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / "src"))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

# Пример использования
student = Student("Иванов Иван", "2000-05-15", "SE-01", 4.5)
print(student)
print(f"Возраст: {student.age()} лет")
```

---

## 🔧 Проверка установки Python

Проверьте, что Python установлен:
```bash
python --version
```

Должно показать что-то вроде: `Python 3.x.x`

Если не работает, попробуйте:
```bash
python3 --version
```
или
```bash
py --version
```

---

## 📂 Проверка, что вы в правильной папке

Выполните:
```bash
dir
```

Вы должны увидеть:
- `run_lab08.py`
- `test_lab08.py`
- `src/` (папка)
- `README.md`

---

## 🚀 Примеры использования в коде

### Создание студента:
```python
from lab08.models import Student

student = Student(
    fio="Иванов Иван Иванович",
    birthdate="2000-05-15",
    group="SE-01",
    gpa=4.5
)
print(student)
```

### Сохранение в JSON:
```python
from lab08.serialize import students_to_json

students = [student]
students_to_json(students, "src/lab08/data/output.json")
```

### Загрузка из JSON:
```python
from lab08.serialize import students_from_json

students = students_from_json("src/lab08/data/students_input.json")
for s in students:
    print(s)
```

---

## ❗ Если что-то не работает

1. **Убедитесь, что вы в корне проекта:**
   ```bash
   cd C:\Users\semen\.ssh\python_labs
   ```

2. **Проверьте наличие файлов:**
   ```bash
   dir run_lab08.py
   dir src\lab08\models.py
   ```

3. **Если ошибка "ModuleNotFoundError":**
   - Убедитесь, что запускаете из корня проекта
   - Проверьте, что файлы `src/lab08/models.py` и `src/lab08/serialize.py` существуют

