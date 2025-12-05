"""
Простой пример использования lab08
Запуск: python test_lab08.py
"""
import sys
from pathlib import Path

# Добавляем src в путь
sys.path.insert(0, str(Path(__file__).parent / "src"))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

def main():
    print("=" * 50)
    print("Пример использования lab08")
    print("=" * 50)
    print()
    
    # 1. Создание студентов
    print("1. Создание объектов Student:")
    print("-" * 50)
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.5
    )
    
    student2 = Student(
        fio="Петрова Мария Сергеевна",
        birthdate="2001-08-22",
        group="IKBO-12",
        gpa=4.8
    )
    
    print(f"  {student1}")
    print(f"  Возраст: {student1.age()} лет")
    print(f"  {student2}")
    print(f"  Возраст: {student2.age()} лет")
    print()
    
    # 2. Сериализация в словарь
    print("2. Сериализация в словарь:")
    print("-" * 50)
    student_dict = student1.to_dict()
    print(f"  to_dict(): {student_dict}")
    
    student_restored = Student.from_dict(student_dict)
    print(f"  from_dict(): {student_restored}")
    print()
    
    # 3. Сохранение в JSON
    print("3. Сохранение списка студентов в JSON:")
    print("-" * 50)
    students_list = [student1, student2]
    output_path = Path("src/lab08/data/students_output.json")
    students_to_json(students_list, output_path)
    print(f"  Сохранено в: {output_path}")
    print()
    
    # 4. Загрузка из JSON
    print("4. Загрузка студентов из JSON:")
    print("-" * 50)
    input_path = Path("src/lab08/data/students_input.json")
    if input_path.exists():
        loaded_students = students_from_json(input_path)
        print(f"  Загружено студентов: {len(loaded_students)}")
        for student in loaded_students:
            print(f"    - {student}, возраст: {student.age()} лет")
    else:
        print(f"  Файл {input_path} не найден")
    print()
    
    print("=" * 50)
    print("Готово!")

if __name__ == "__main__":
    main()

