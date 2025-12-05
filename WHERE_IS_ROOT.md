# Где находится корень проекта?

## Корень проекта - это:

**`C:\Users\semen\.ssh\python_labs\`**

Это папка, где находятся:
- ✅ `README.md`
- ✅ `pyproject.toml`
- ✅ `run_lab08.py`
- ✅ `test_lab08.py`
- ✅ папка `src/`
- ✅ папка `tests/`

## Как открыть терминал в корне проекта:

### Способ 1: Через проводник Windows
1. Откройте проводник
2. Перейдите в `C:\Users\semen\.ssh\python_labs`
3. В адресной строке введите `cmd` и нажмите Enter
   - Или введите `powershell` и нажмите Enter

### Способ 2: Через командную строку
```cmd
cd C:\Users\semen\.ssh\python_labs
```

### Способ 3: Через PowerShell
```powershell
cd C:\Users\semen\.ssh\python_labs
```

## Проверка, что вы в корне:

Выполните команду:
```bash
dir
```

Вы должны увидеть файлы:
- `README.md`
- `pyproject.toml`
- `run_lab08.py`
- `test_lab08.py`
- папку `src`

## Примеры путей относительно корня:

```
python_labs/                          ← корень
├── run_lab08.py                      ← файл в корне
├── src/                              ← папка в корне
│   └── lab08/
│       ├── models.py                 ← src/lab08/models.py
│       └── data/
│           └── students_input.json   ← src/lab08/data/students_input.json
```

## Запуск из корня:

Когда вы находитесь в корне проекта (`C:\Users\semen\.ssh\python_labs`), 
выполняйте команды:

```bash
python run_lab08.py
```

или

```bash
python test_lab08.py
```

## Если вы в другой папке:

Если вы находитесь, например, в `src/lab08/`, то нужно либо:
1. Вернуться в корень: `cd ..\..\`
2. Или указать полный путь: `python ..\..\run_lab08.py`

