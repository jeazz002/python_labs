def format_record(rec: tuple[str, str, float]):
    fio, group, gpa = rec
    fio = " ".join(fio.strip().split())
    group = group.strip()
    parts = fio.split()
    surname = parts[0].title()
    initials = ""
    if len(parts) > 1:
        for name in parts[1:3]:
            initials += name[0].upper() + "."
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
rec = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("  cидорова  анна   сергеевна ", "ABB-01", 3.999)
]
print(format_record(rec))