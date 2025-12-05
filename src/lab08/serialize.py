import json
from pathlib import Path
from .models import Student

def students_to_json(students: list[Student], path: str | Path) -> None:
    data = [s.to_dict() for s in students]
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json_str)

def students_from_json(path: str | Path) -> list[Student]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    students = []
    for item in data:
        student = Student.from_dict(item)
        students.append(student)
    
    return students

