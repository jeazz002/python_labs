# Команды для lab07

## 1. Установка зависимостей

```powershell
pip install pytest
```

## 2. Запуск всех тестов

```powershell
python -m pytest tests/ -v
```

## 3. Запуск конкретного файла тестов

```powershell
# Тесты для text.py
python -m pytest tests/test_text.py -v

# Тесты для json_csv.py
python -m pytest tests/test_json_csv.py -v
```

## 4. Запуск конкретного теста

```powershell
python -m pytest tests/test_text.py::test_normalize_basic -v
```

## 5. Проверка стиля кода с black

```powershell
# Установка black (если еще не установлен)
pip install black

# Проверка стиля без изменений (только показывает, что нужно исправить)
black --check src/ tests/

# Автоматическое исправление стиля кода
black src/ tests/

# Проверка конкретного файла
black --check tests/test_text.py

# Показать, что будет изменено (без реальных изменений)
black --diff src/ tests/
```

